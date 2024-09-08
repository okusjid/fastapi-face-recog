from app.config.celery_config import celery_app
import time

# Face recognition task
@celery_app.task
def process_face_recognition(data):
    time.sleep(5)  # Simulate a long-running task
    return {"status": "Processed", "data": data}

# Web crawler task
@celery_app.task
def run_crawler(url):
    from app.services.Crawler import main as crawl
    result = crawl(url)
    return result
