import joblib
import numpy as np 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, '..', 'model', 'model.pkl')
scaler_path = os.path.join(BASE_DIR, '..', 'model', 'scaler.pkl')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def model_predict(data):
    data = scaler.transform(data)
    result = model.predict(data)
    return result[0]