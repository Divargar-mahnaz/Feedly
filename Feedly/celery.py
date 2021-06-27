import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Feedly.settings')

app = Celery('Feedly')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
