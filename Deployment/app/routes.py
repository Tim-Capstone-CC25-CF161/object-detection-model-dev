from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
import tensorflow as tf
import numpy as np
import logging
import io
from PIL import Image
from utils.utils import load_model, detect_animals_in_image, category_index

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define router
router = APIRouter()

# Global model
model_fn = None

class Detection(BaseModel):
    animal_name: str
    bounding_box: List[float]
    confidence: float

class PredictionResponse(BaseModel):
    detections: List[Detection]

@router.on_event("startup")
async def startup_event():
    global model_fn
    model_path = "./model"
    try:
        model_fn = load_model(model_path, logger)
        logger.info("Model loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading model: {e}")

@router.get("/")
async def root():
    model_status = "loaded" if model_fn is not None else "not loaded"
    return {
        "message": "TensorFlow Model API is running",
        "model_status": model_status
    }

@router.get("/health")
async def health_check():
    if model_fn is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {
        "status": "healthy",
        "model_loaded": True,
        "tensorflow_version": tf.__version__
    }

@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    pil_image = Image.open(io.BytesIO(contents))

    detections = detect_animals_in_image(
        pil_image,
        model_fn=model_fn,
        category_index=category_index,
        input_image_size=(640, 640),
        min_score_thresh=0.3
    )

    return PredictionResponse(detections=detections)
