from django.contrib.auth import get_user_model
from .models import *
from celery import shared_task
from django.core.mail import send_mail
from celeryproject import settings
from django.utils import timezone
from datetime import timedelta

@shared_task(bind=True)
def activate(self):
    d=Demo.objects.all()
    for x in d:
        x.is_active=True
        x.save()

    return 'yes'