import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

"""df = pd.read_csv('phishing_dataset.csv')
X = df.drop('label', axis=1)
y = df['label']
model = RandomForestClassifier()
model.fit(X, y)"""
def train_model_if_missing():
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier

    df = pd.read_csv('phishing_dataset.csv')  # ensure this exists
    X = df.drop('label', axis=1)
    y = df['label']
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, 'phishing_model.pkl')


joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")