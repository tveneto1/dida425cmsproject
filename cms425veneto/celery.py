import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms425veneto.settings")

# Create Celery app instance
app = Celery("cms425veneto")

# Load Celery settings from Django settings.py using the CELERY namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py files in installed apps
app.autodiscover_tasks()
