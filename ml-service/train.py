import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import f1_score, recall_score, accuracy_score, precision_score, confusion_matrix
import pickle

# The entire pipeline structured:
# 1. load the data
# 2. provide the labels to each data file 
# 3. combine the datasets and shuffle it using the ignore index 
# 4. clean the text using the function and remove the reuters word from the dataset
# 5. vectorise it using the tfidf vectoriser, set the maxfeatures, ngram range and also the stop words removal
# 6. set the train test split 
# 7. bring the svm model and train it
# 8. evaluate the metrics 
# 9. save the model

true_df = pd.read_csv("datasets/true.csv")
fake_df = pd.read_csv("datasets/fake.csv")

true_df['label'] = 1
fake_df['label'] = 0

news_df = pd.concat([true_df, fake_df], ignore_index=True)
news_df = news_df.sample(frac=1, random_state=42).reset_index(drop=True)

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'reuters', '', text)  
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

news_df['text'] = news_df['text'].apply(clean_text)


texts = news_df['text'].values
labels = news_df['label'].values

vectorizer = TfidfVectorizer(max_features=6000, ngram_range=(1,2), stop_words='english')
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_predict = model.predict(X_test)

print("MODEL: SVM")
print(f"Accuracy: {accuracy_score(y_test, y_predict)}")
print(f"Recall Score: {recall_score(y_test, y_predict)}")
print(f"Precision Score: {precision_score(y_test, y_predict)}")
print(f"F1 Score: {f1_score(y_test, y_predict)}")
print(f"Confusion Matrix: {confusion_matrix(y_test, y_predict)}")

# Save model and vectorizer
with open('model/svm_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("\nModel and vectorizer saved!")




