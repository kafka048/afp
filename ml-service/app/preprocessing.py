import re

def preprocessing_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'reuters', '', text)  
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()


    return text

