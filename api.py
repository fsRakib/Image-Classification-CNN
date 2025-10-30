"""
FastAPI Backend for Cat vs Dog Image Classification
Provides RESTful API endpoints for the trained CNN model
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tensorflow import keras
import numpy as np
from PIL import Image
import io
import gdown
import os
from typing import Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Cat vs Dog Classifier API",
    description="Deep Learning API for classifying images as cats or dogs using CNN",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware - Allow all origins (configure based on your needs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model configuration
MODEL_PATH = "dogs_vs_cats_production_model.keras"
GDRIVE_FILE_ID = "1NUmowM-IX9yRhsNad1G42042YAEzYVig"
IMG_SIZE = (128, 128)
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

# Global model variable
model = None


def download_model() -> None:
    """Download the trained model from Google Drive if not present"""
    if not os.path.exists(MODEL_PATH):
        logger.info("Model not found. Downloading from Google Drive...")
        try:
            url = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"
            gdown.download(url, MODEL_PATH, quiet=False)
            logger.info("Model downloaded successfully!")
        except Exception as e:
            logger.error(f"Failed to download model: {e}")
            raise HTTPException(
                status_code=500,
                detail="Failed to download model from Google Drive"
            )


def load_model() -> keras.Model:
    """Load the trained Keras model"""
    global model
    if model is None:
        try:
            download_model()
            model = keras.models.load_model(MODEL_PATH)
            logger.info("Model loaded successfully!")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to load model: {str(e)}"
            )
    return model


def validate_image(file: UploadFile) -> None:
    """Validate uploaded image file"""
    # Check file extension
    file_ext = file.filename.split(".")[-1].lower() if file.filename else ""
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Check file size (max 10MB)
    file.file.seek(0, 2)  # Seek to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset to beginning
    
    max_size = 10 * 1024 * 1024  # 10MB
    if file_size > max_size:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size: {max_size / (1024*1024)}MB"
        )


def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Preprocess image for model prediction
    
    Args:
        image: PIL Image object
        
    Returns:
        Preprocessed numpy array ready for model input
    """
    # Convert to RGB (handle RGBA, grayscale, etc.)
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resize to model's expected input size
    image = image.resize(IMG_SIZE)
    
    # Convert to numpy array and normalize to [0, 1]
    img_array = np.array(image) / 255.0
    
    # Add batch dimension: (1, 128, 128, 3)
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array


def get_prediction_details(prediction_score: float) -> Dict[str, Any]:
    """
    Convert raw prediction score to detailed results
    
    Args:
        prediction_score: Model output (0.0 to 1.0)
        
    Returns:
        Dictionary with prediction details
    """
    # Binary classification: > 0.5 = Dog, <= 0.5 = Cat
    is_dog = prediction_score > 0.5
    
    # Calculate confidence as distance from decision boundary
    confidence = prediction_score if is_dog else (1 - prediction_score)
    
    return {
        "prediction": "Dog" if is_dog else "Cat",
        "confidence": round(float(confidence * 100), 2),  # Percentage
        "raw_score": round(float(prediction_score), 4),
        "probabilities": {
            "cat": round(float(1 - prediction_score) * 100, 2),
            "dog": round(float(prediction_score) * 100, 2)
        }
    }


# API Endpoints

@app.on_event("startup")
async def startup_event():
    """Load model on application startup"""
    logger.info("Starting Cat vs Dog Classifier API...")
    load_model()
    logger.info("API ready to accept requests!")


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Cat vs Dog Classifier API",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "predict": "/predict (POST)",
            "health": "/health (GET)",
            "model_info": "/model/info (GET)",
            "docs": "/docs (Interactive API documentation)"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        model_loaded = model is not None
        return {
            "status": "healthy" if model_loaded else "unhealthy",
            "model_loaded": model_loaded,
            "model_path": MODEL_PATH,
            "model_exists": os.path.exists(MODEL_PATH)
        }
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "error": str(e)}
        )


@app.get("/model/info")
async def model_info():
    """Get information about the loaded model"""
    try:
        current_model = load_model()
        return {
            "model_name": "Dogs vs Cats CNN Classifier",
            "model_type": "Convolutional Neural Network",
            "input_shape": (128, 128, 3),
            "output_classes": ["Cat", "Dog"],
            "model_size_mb": round(os.path.getsize(MODEL_PATH) / (1024 * 1024), 2),
            "framework": "TensorFlow/Keras",
            "training_accuracy": "~92%",
            "supported_formats": list(ALLOWED_EXTENSIONS)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    """
    Predict whether the uploaded image contains a cat or dog
    
    Args:
        file: Image file (JPG, JPEG, PNG)
        
    Returns:
        JSON with prediction, confidence, and probabilities
    """
    try:
        # Validate file
        validate_image(file)
        
        # Read and process image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Preprocess for model
        processed_image = preprocess_image(image)
        
        # Get model and make prediction
        current_model = load_model()
        prediction = current_model.predict(processed_image, verbose=0)
        prediction_score = prediction[0][0]
        
        # Get detailed results
        result = get_prediction_details(prediction_score)
        
        logger.info(f"Prediction: {result['prediction']} ({result['confidence']}%)")
        
        return {
            "success": True,
            "filename": file.filename,
            "prediction": result["prediction"],
            "confidence_percentage": result["confidence"],
            "raw_score": result["raw_score"],
            "probabilities": result["probabilities"],
            "metadata": {
                "image_size": image.size,
                "image_mode": image.mode,
                "model_input_size": IMG_SIZE
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


@app.post("/predict/batch")
async def predict_batch(files: list[UploadFile] = File(...)):
    """
    Predict multiple images in a single request
    
    Args:
        files: List of image files
        
    Returns:
        JSON with predictions for each image
    """
    if len(files) > 10:
        raise HTTPException(
            status_code=400,
            detail="Maximum 10 images allowed per batch request"
        )
    
    results = []
    
    for file in files:
        try:
            validate_image(file)
            contents = await file.read()
            image = Image.open(io.BytesIO(contents))
            processed_image = preprocess_image(image)
            
            current_model = load_model()
            prediction = current_model.predict(processed_image, verbose=0)
            prediction_score = prediction[0][0]
            
            result = get_prediction_details(prediction_score)
            
            results.append({
                "filename": file.filename,
                "success": True,
                "prediction": result["prediction"],
                "confidence_percentage": result["confidence"],
                "probabilities": result["probabilities"]
            })
            
        except Exception as e:
            results.append({
                "filename": file.filename,
                "success": False,
                "error": str(e)
            })
    
    return {
        "success": True,
        "total_images": len(files),
        "results": results
    }


if __name__ == "__main__":
    import uvicorn
    
    # Run the API server
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes (disable in production)
        log_level="info"
    )
