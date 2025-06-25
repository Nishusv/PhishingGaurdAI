import joblib
from feature_extractor import extract_features

model = joblib.load('phishing_model.pkl')

def is_phishing(url):
    features = extract_features(url)
    prediction = model.predict([features])
    probability = model.predict_proba([features])[0][1]
    return prediction[0], probability