from fastapi import FastAPI
from ml_service.app.schemas import NewsRequest, PredictionResponse
from ml_service.app.predictor import FakeNewsPredictor

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

FRONTEND_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "web-app"
    / "dist"
)

if FRONTEND_DIR.exists():
    app.mount(
        "/assets",
        StaticFiles(directory=FRONTEND_DIR / "assets"),
        name="assets"
    )

predictor = FakeNewsPredictor()


@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.post("/predict", response_model=PredictionResponse)
def predict_news(request: NewsRequest):
    news = request.text
    return predictor.predict_news(news)


@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    file_path = FRONTEND_DIR / full_path

    if file_path.exists():
        return FileResponse(file_path)

    return FileResponse(FRONTEND_DIR / "index.html")