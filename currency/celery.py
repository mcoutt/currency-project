import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency.settings')

app = Celery(os.getenv("CELERY_QUEUE"))

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = os.getenv("CELERY_BROKER_URL")
app.conf.result_backend = os.getenv("CELERY_RESULT_BACKEND_URL")

app.autodiscover_tasks()
