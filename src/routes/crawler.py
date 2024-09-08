from fastapi import APIRouter, BackgroundTasks
from src.celery_worker import run_crawler

router = APIRouter()

@router.post("/start-crawl/")
async def start_crawl(
    background_tasks: BackgroundTasks,
    skip: bool = True,
    threads: int = 4,
    google: bool = True,
    naver: bool = True,
    full_resolution: bool = False,
    face: bool = False,
    no_gui: str = 'auto',
    limit: int = 0,
    proxy_list: str = ''
):
    # Add the task to Celery with the parameters
    background_tasks.add_task(run_crawler, skip, threads, google, naver, full_resolution, face, no_gui, limit, proxy_list)
    return {"message": "Crawler started"}
