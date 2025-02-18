# coding=utf-8
from django.contrib import admin
from .models import Subscriber, EmailCampaign


# Регистрация модели Subscriber
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'birth_date')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('birth_date',)


# Регистрация модели EmailCampaign
@admin.register(EmailCampaign)
class EmailCampaignAdmin(admin.ModelAdmin):
    list_display = ('subject', 'scheduled_time', 'created_at')
    search_fields = ('subject',)
    list_filter = ('scheduled_time', 'created_at')
