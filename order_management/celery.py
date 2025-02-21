import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "order_management.settings")

app = Celery("order_management")

# Load Celery configuration from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in Django apps
app.autodiscover_tasks()
