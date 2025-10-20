# main.py - FastAPI Backend for Heart Disease Prediction

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import uvicorn

from model.prediction import predict_output, model
from data_validation.input_data_validation import HeartDiseaseInput
from data_validation.response_data_validation import PredictionResponse

# Initialize FastAPI app
app = FastAPI(
    title="Heart Disease Prediction API",
    description="AI-powered heart disease prediction using machine learning",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Heart Disease Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "prediction": "/predict",
            "health": "/health",
            "docs": "/docs"
        },
        "model_status": "loaded" if model is not None else "not loaded"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict_heart_disease(input_data: HeartDiseaseInput):
    """
    Predict heart disease based on patient data
    
    Returns:
        - prediction: 0 (no disease) or 1 (disease present)
        - probability: confidence score (if available)
        - risk_level: "Low Risk" or "High Risk"
        - message: descriptive message
    """
    
    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded. Please ensure model.pkl is in the correct directory."
        )
    
    try:
        # Prepare input data as numpy array
        # Order must match the training data features
        features = np.array([[
            input_data.age,
            input_data.sex,
            input_data.cp,
            input_data.trestbps,
            input_data.chol,
            input_data.fbs,
            input_data.restecg,
            input_data.thalach,
            input_data.exang,
            input_data.oldpeak,
            input_data.slope,
            input_data.ca,
            input_data.thal
        ]]).reshape(1, -1)
        
        # Make prediction
        prediction = predict_output(features)
        
        return prediction
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )
    

@app.get("/model-info")
async def model_info():
    """Get information about the loaded model"""
    
    if model is None:
        return {"status": "Model not loaded"}
    
    info = {
        "model_type": type(model).__name__,
        "features": [
            "age", "sex", "cp", "trestbps", "chol", "fbs", 
            "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ],
        "has_probability": hasattr(model, 'predict_proba')
    }
    
    # Add additional model-specific information
    if hasattr(model, 'n_features_in_'):
        info["n_features"] = model.n_features_in_
    
    if hasattr(model, 'feature_importances_'):
        info["has_feature_importance"] = True
    
    return info

# Run the application
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 Starting Heart Disease Prediction API")
    print("="*60)
    print("\n📋 Instructions:")
    print("1. Make sure 'model.pkl' is in the same directory as this file")
    print("2. The API will run on http://localhost:8000")
    print("3. Access API documentation at http://localhost:8000/docs")
    print("4. Test the API at http://localhost:8000/docs#/default/predict_heart_disease_predict_post")
    print("\n" + "="*60 + "\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )