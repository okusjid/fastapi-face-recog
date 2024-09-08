# fastapi/app.py
from fastapi import FastAPI
from .routes import crawler

app = FastAPI()

# Include the face recognition and crawler routes
# app.include_router(face_recognition.router)
app.include_router(crawler.router)
