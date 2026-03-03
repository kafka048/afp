from pydantic import BaseModel

class NewsRequest(BaseModel):
    text : str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    is_fake : bool