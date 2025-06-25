"""import joblib
from feature_extractor import extract_features

model = joblib.load('phishing_model.pkl')

def is_phishing(url):
    features = extract_features(url)
    prediction = model.predict([features])
    probability = model.predict_proba([features])[0][1]
    return prediction[0], probability"""
import os
import joblib
from feature_extractor import extract_features
from model_trainer import train_model_if_missing

MODEL_PATH = 'phishing_model.pkl'

if not os.path.exists(MODEL_PATH):
    train_model_if_missing()  # dynamically generate model

model = joblib.load(MODEL_PATH)

def is_phishing(url):
    features = extract_features(url)
    prediction = model.predict([features])
    probability = model.predict_proba([features])[0][1]
    return prediction[0], probability
