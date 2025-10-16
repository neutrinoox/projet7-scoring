from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import pickle
import pandas as pd
import numpy as np
import uvicorn
import os

app = FastAPI(title="Credit Scoring API", version="1.0.0")

MODEL_DIR = os.getenv("MODEL_DIR", "./models")

# Charge les modèles
with open(f'{MODEL_DIR}/lgbm_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open(f'{MODEL_DIR}/imputer.pkl', 'rb') as f:
    imputer = pickle.load(f)
with open(f'{MODEL_DIR}/feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)

class ClientFeatures(BaseModel):
    data: Dict[str, Optional[float]]
    client_id: Optional[str] = None

class PredictionResult(BaseModel):
    client_id: Optional[str]
    default_probability: float
    prediction: str
    risk_level: str

def preprocess_data(client_data: Dict) -> pd.DataFrame:
    df = pd.DataFrame([client_data])
    for feature in feature_names:
        if feature not in df.columns:
            df[feature] = np.nan
    df = df[feature_names]
    return pd.DataFrame(imputer.transform(df), columns=feature_names)

@app.get("/")
def root():
    return {"message": "Credit Scoring API", "status": "active"}

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict", response_model=PredictionResult)
def predict(client: ClientFeatures):
    try:
        df = preprocess_data(client.data)
        proba = float(model.predict_proba(df)[0, 1])
        
        decision = "REFUSÉ" if proba >= 0.5 else "ACCEPTÉ"
        
        if proba < 0.3:
            risk = "FAIBLE"
        elif proba < 0.6:
            risk = "MOYEN"
        else:
            risk = "ÉLEVÉ"
        
        return PredictionResult(
            client_id=client.client_id,
            default_probability=round(proba, 4),
            prediction=decision,
            risk_level=risk
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
