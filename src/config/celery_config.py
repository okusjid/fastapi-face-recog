from celery import Celery

celery_app = Celery(
    "face_recognition_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.update(
    result_expires=3600,
)
