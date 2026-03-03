from fastapi import FastAPI
from schemas import NewsRequest, PredictionResponse
from predictor import FakeNewsPredictor

app = FastAPI()
predictor = FakeNewsPredictor()

@app.get("/")
def health_root() -> dict[str, str]:
    return {
        'message' : 'API active and running'
    }

@app.post("/predict", response_model=PredictionResponse)
def predict_news(request: NewsRequest):
    news = request.text
    return predictor.predict_news(news)



