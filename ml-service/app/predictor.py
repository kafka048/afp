import pickle
from preprocessing import preprocessing_text
from pathlib import Path


class FakeNewsPredictor:
    def __init__(self) -> None:        
        self.model = self.load_model()
        self.vectoriser = self.load_vectoriser()

    def load_model(self):
        model_path = Path(__file__).parent.parent / 'model' / 'svm_model.pkl'
        with open(model_path, 'rb') as f:
            return pickle.load(f)
        
    def load_vectoriser(self):
        vectoriser_path = Path(__file__).parent.parent / 'model' / 'vectorizer.pkl'
        with open(vectoriser_path, 'rb') as f:
            return pickle.load(f)
        

    def predict_news(self, text: str):
        clean_text = preprocessing_text(text)
        X = self.vectoriser.transform([clean_text])
        prediction = self.model.predict(X)[0]
        decision_score = self.model.decision_function(X)[0]
        confidence_score = (abs(decision_score) / (1 + abs(decision_score)) * 100)

        return prediction, confidence_score
    
    def format_prediction(self, prediction: int, confidence_score: float) -> dict[str, str | float | bool]:
        is_fake = (prediction == 0)
        label = 'Fake News' if is_fake else 'Real News'
        confidence_metric = round(confidence_score, 2)

        return {
            'prediction' : label,
            'confidence' : confidence_metric,
            'is_fake' : is_fake
        }

        
        
         
        


        
        
            

         
