# Backend - FastAPI app for AI Image Caption Generator


from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import io


# Load BLIP model and processor at startup
app = FastAPI()
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/caption")
async def generate_caption(file: UploadFile = File(...)) -> Dict[str, str]:
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return {"caption": caption}

@app.get("/")
def root():
    return {"message": "AI Image Caption Generator Backend"}
