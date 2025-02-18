# -*- coding: utf-8 -*-
from django import forms
from .models import EmailCampaign


class EmailCampaignForm(forms.ModelForm):
    class Meta:
        model = EmailCampaign
        fields = ['subject', 'html_template', 'scheduled_time']
        widgets = {
            'html_template': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'scheduled_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        }

    def clean_scheduled_time(self):
        scheduled_time = self.cleaned_data.get('scheduled_time')
        if scheduled_time:
            try:
                # Проверяем, что дата введена в правильном формате
                from datetime import datetime
                datetime.strptime(scheduled_time, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise forms.ValidationError(u"Введите дату в формате YYYY-MM-DD HH:MM:SS")
        return scheduled_time
