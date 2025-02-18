# -*- coding: utf-8 -*-
import logging
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from .forms import EmailCampaignForm
from .tasks import send_email_campaign
from .models import Subscriber

logger = logging.getLogger(__name__)


def create_campaign(request):
    """
    Обработчик для создания новой email-кампании.
    """
    if request.method == 'POST':
        form = EmailCampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            try:
                # Если время запланировано, отправляем задачу Celery с eta
                if campaign.scheduled_time and campaign.scheduled_time > now():
                    send_email_campaign.apply_async((campaign.id,), eta=campaign.scheduled_time)
                else:
                    # Если время не запланировано, отправляем сразу
                    send_email_campaign.delay(campaign.id)
                return JsonResponse({'success': True})
            except Exception as e:
                logger.error(u"Ошибка при отправке задачи Celery: {}".format(e))
                return JsonResponse({'success': False, 'errors': u'Ошибка при отправке задачи'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'emails/modal_form.html', {'form': EmailCampaignForm()})


def track_open(request, subscriber_id):
    """
    Обработчик для отслеживания открытия письма.
    """
    try:
        # Находим подписчика по ID
        subscriber = Subscriber.objects.get(id=subscriber_id)
        # Обновляем статус открытия
        subscriber.email_opened = True
        subscriber.opened_at = now()
        subscriber.save()
        logger.info(u"Письмо открыто подписчиком: {}".format(subscriber.email))
        return HttpResponse('')
    except Subscriber.DoesNotExist:
        logger.warning(u"Подписчик с ID {} не найден".format(subscriber_id))
        return HttpResponse(u'Subscriber not found', status=404)
