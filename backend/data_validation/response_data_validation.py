from pydantic import BaseModel
from typing import Optional

class PredictionResponse(BaseModel):
    prediction: int
    probability: Optional[float] = None
    risk_level: str
    message: str