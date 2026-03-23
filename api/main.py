from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
from src.predict import model_predict
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class PatientData(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    dpf: float
    age: float

@app.post('/predict')
def predict(
    data:PatientData
):
    df = pd.DataFrame({
    'Pregnancies':[data.pregnancies],
    'Glucose':[data.glucose],
    'BloodPressure':[data.blood_pressure],
    'SkinThickness':[data.skin_thickness],
    'Insulin':[data.insulin],
    'BMI':[data.bmi],
    'DiabetesPedigreeFunction':[data.dpf],
    'Age':[data.age],    
    })

    prediction = model_predict(df)

    if prediction==0:
        return {'prediction':'The Patient is Clear'}
    else:
        return {'prediction':'The Patient has Diabetes'}
    
    