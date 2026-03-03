from fastapi import FastAPI
from schemas import NewsRequest, PredictionResponse
from predictor import FakeNewsPredictor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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



