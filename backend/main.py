# Backend - FastAPI app for AI Image Caption Generator

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/caption")
async def generate_caption(file: UploadFile = File(...)) -> Dict[str, str]:
    # Placeholder: Replace with actual AI model inference
    return {"caption": "A placeholder caption for the uploaded image."}

@app.get("/")
def root():
    return {"message": "AI Image Caption Generator Backend"}
