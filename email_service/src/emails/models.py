# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    """
        Модель для хранения данных подписчиков.
        Поля:
            email (EmailField): Уникальный email подписчика.
            first_name (CharField): Имя подписчика (максимум 100 символов).
            last_name (CharField): Фамилия подписчика (максимум 100 символов).
            birth_date (DateField): Дата рождения подписчика (необязательное поле).
        Методы:
            __unicode__: Возвращает email подписчика для отображения в интерфейсе Django Admin.
        """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.email


class EmailCampaign(models.Model):
    """
        Модель для хранения данных о рассылках.
        Поля:
            subject (CharField): Тема письма (максимум 255 символов).
            html_template (TextField): HTML-шаблон письма.
            scheduled_time (DateTimeField): Время запланированной отправки (необязательное поле).
            created_at (DateTimeField): Время создания записи (автоматически устанавливается при создании).
        Методы:
            __unicode__: Возвращает тему письма для отображения в интерфейсе Django Admin.
        """
    subject = models.CharField(max_length=255)
    html_template = models.TextField()
    scheduled_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject
