# coding=utf-8
from celery import shared_task
from django.core.mail import send_mail
from django.template import Template, Context
from .models import Subscriber, EmailCampaign
import json


@shared_task
def send_email_campaign(campaign_id):
    try:
        # Получаем кампанию
        campaign = EmailCampaign.objects.get(id=campaign_id)
        # Получаем всех подписчиков
        subscribers = Subscriber.objects.all()

        for subscriber in subscribers:
            # Рендерим шаблон с использованием Django Template Engine
            html_template = Template(campaign.html_template)
            context = Context({
                'first_name': subscriber.first_name,
                'last_name': subscriber.last_name,
                'subscriber_id': subscriber.id
            })
            rendered_html = html_template.render(context)

            # Формируем данные для логирования в JSON
            message_data = {
                u"subject": campaign.subject,
                u"message": rendered_html,
                u"recipient": subscriber.email
            }

            # Логируем данные в формате JSON
            print(u"Sending email: {}".format(json.dumps(message_data, ensure_ascii=False)))

            # Отправляем письмо
            send_mail(
                subject=campaign.subject,
                message=u'',
                from_email=u'vladvorobei94@mail.ru',
                recipient_list=[subscriber.email],
                html_message=rendered_html
            )
            print(u"Email sent to {}".format(subscriber.email))
    except Exception as e:
        print(u"Error sending email: {}".format(e))
