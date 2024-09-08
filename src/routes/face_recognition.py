from fastapi import APIRouter, BackgroundTasks
from src.celery_worker import process_face_recognition

router = APIRouter()

@router.post("/recognize-face/")
async def recognize_face(data: dict, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_face_recognition, data)
    return {"message": "Face recognition task submitted"}
