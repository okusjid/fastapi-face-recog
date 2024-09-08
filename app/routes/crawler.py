from fastapi import APIRouter, BackgroundTasks
from app.celery_worker import run_crawler

router = APIRouter()

@router.post("/start-crawl/")
async def start_crawl(url: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_crawler, url)
    return {"message": f"Crawler started for {url}"}
