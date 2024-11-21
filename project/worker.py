import os
import time

from celery import Celery, Task


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_type):
    try:
        t = int(task_type)*10
        time.sleep(t)
    except ValueError:
        t = time.time()
        time.sleep(2)
        raise IndexError("TWAT.F.")
    return t
