# THE ACTUAL FOURTH PILLAR

An AI-powered full-stack fake news classification system designed to analyze news articles using machine learning and provide confidence-calibrated predictions through a cinematic intelligence-console interface.

---

## Overview

THE ACTUAL FOURTH PILLAR is a production-deployed ML inference system that classifies news articles as either **Real** or **Fake** using a TF-IDF + Linear SVM pipeline.

The project was built to go beyond notebook experimentation and into real-world deployment architecture by integrating:

* Machine Learning inference
* FastAPI backend services
* React frontend interface
* Tailwind-based intelligence-console UI
* Production deployment pipeline
* Confidence interpretation system
* Single-server frontend/backend integration

The system evaluates linguistic structure, journalistic tone, and textual patterns to generate predictions and calibrated confidence scores.

> **Note:** The current model evaluates linguistic patterns and writing structure; not factual truth or real-world validity.

---

## Live Deployment

Deployed on Render.

```text
https://afp-4q4e.onrender.com/
```

---

## Features

### Machine Learning

* TF-IDF Vectorization
* Linear SVM Classification
* Probability Calibration using `predict_proba()`
* Confidence score generation
* Structured inference pipeline
* Encapsulated prediction service

### Backend

* FastAPI REST API
* Pydantic request/response validation
* Static frontend serving via FastAPI
* Production-safe package architecture
* Deployment-safe model loading using `Path()`

### Frontend

* React + Vite + TypeScript
* Tailwind CSS v4
* Cinematic dark-themed intelligence console
* Real-time prediction rendering
* Confidence visualization bars
* Dynamic uncertainty interpretation
* Error handling + loading states

### Deployment

* Single-service deployment architecture
* Render deployment pipeline
* Integrated frontend/backend serving
* Production-ready structure

---

## Tech Stack

### Frontend

* React
* Vite
* TypeScript
* Tailwind CSS v4
* Axios

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Linear SVM
* NumPy
* Pandas

---

## Project Structure

```text
AFP/
├── ml_service/
│   ├── app/
│   │   ├── main.py
│   │   ├── predictor.py
│   │   ├── preprocessing.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   │
│   ├── model/
│   │   ├── svm_model.pkl
│   │   └── vectorizer.pkl
│   │
│   ├── requirements.txt
│   └── venv/
│
├── web-app/
│   ├── src/
│   ├── public/
│   ├── dist/
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```

---

## How It Works

```text
User Input
    ↓
Frontend Intelligence Console
    ↓
POST /predict
    ↓
FastAPI Backend
    ↓
ML Inference Pipeline
    ↓
Prediction + Confidence
    ↓
Frontend Visualization
```

---

## Model Pipeline

The current model follows a clean anti-data-leakage workflow:

1. Load datasets
2. Label fake/real data
3. Shuffle dataset
4. Preprocess text
5. Split train/test data
6. Fit TF-IDF on training set only
7. Transform datasets
8. Train Linear SVM
9. Generate calibrated probabilities
10. Save trained artifacts

---

## Confidence Interpretation

The UI categorizes predictions into operational confidence bands:

| Confidence | Interpretation            |
| ---------- | ------------------------- |
| < 55%      | Low confidence            |
| 55–75%     | Moderate confidence       |
| > 75%      | High stylistic confidence |

---

## Key Engineering Learnings

* Data leakage prevention matters
* SVM margins are not probabilities
* Confidence calibration improves interpretability
* Style classification is not factual verification
* Clean package architecture simplifies deployment
* Integrated frontend/backend serving reduces deployment complexity

---

## Future Improvements

Planned upgrade directions:

* Transformer-based classification (BERT/DistilBERT)
* Dual-model comparison system
* Database prediction logging
* Retrieval-augmented factual verification
* User authentication
* Prediction history dashboard

---

## Local Development

### Backend

```bash
cd ml_service
source venv/bin/activate
uvicorn ml_service.app.main:app --reload
```

### Frontend

```bash
cd web-app
npm install
npm run dev
```

---

## Deployment

The project is deployed using:

* Render (Backend + Frontend Serving)
* FastAPI static file serving
* Production React build (`dist/`)

Build Command:

```bash
cd web-app && npm install && npm run build && cd ../ml_service && pip install -r requirements.txt
```

Start Command:

```bash
uvicorn ml_service.app.main:app --host 0.0.0.0 --port 10000
```

---

## Author

Amrit Raj

Built as a full-stack machine learning deployment project focused on production architecture, inference
