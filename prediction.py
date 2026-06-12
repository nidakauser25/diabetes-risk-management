import joblib
import numpy as np

model = joblib.load("models/diabetes_model.pkl")

def predict_diabetes(features):
    features = np.array(features).reshape(1, -1)
    return model.predict(features)[0]