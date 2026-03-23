import streamlit as st 
import pandas as pd 
from src.predict import model_predict 

st.title('Diabetes prediction Web App')
st.info('Easy Application for Diabetes Prediction Deses')

# ##Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')

pregnancies = st.number_input('Pregnancies')
glucose = st.number_input('Glucose')
blood_pressure = st.number_input('BloodPressure')
skin_thickness = st.number_input('SkinThickness')
insulin = st.number_input('Insulin')
bmi = st.number_input('BMI')
dpf = st.number_input('DiabetesPedigreeFunction')
age = st.number_input('Age')

df = pd.DataFrame({
    'Pregnancies':[pregnancies],
    'Glucose':[glucose],
    'BloodPressure':[blood_pressure],
    'SkinThickness':[skin_thickness],
    'Insulin':[insulin],
    'BMI':[bmi],
    'DiabetesPedigreeFunction':[dpf],
    'Age':[age],
})

confirm =  st.button('Confirm')

if confirm:
    result = model_predict(df)

    if result == 0:
        st.write('The patient is clear')
    else:
        st.write('The patient is deses')