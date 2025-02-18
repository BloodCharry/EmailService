# coding=utf-8
from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_service.config.settings')

app = Celery('email_service')

app.config_from_object('django.conf:settings')

# Разрешаем использование pickle
app.conf.update(
    task_serializer='pickle',
    accept_content=['pickle'],  # Разрешаем только pickle
    result_serializer='pickle',
)

# Отключаем pickle
app.conf.accept_content = ['json']

app.autodiscover_tasks(['src.emails'])
