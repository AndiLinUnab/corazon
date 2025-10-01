import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import urllib

# Cargar el modelo y el escalador guardados
scaler = joblib.load('scaler.jb')
model = joblib.load('svc_model.jb')

# Título y subtítulo
st.title('Predictor de Problemas Cardiacos')
st.subheader('Elaborado por UNAB 2025')

# Descripción
st.write("""
    Esta aplicación predice si una persona tiene problemas cardiacos según su edad y nivel de colesterol.
    Desliza los controles para ingresar los valores de edad y colesterol.
""")

# Sliders para edad y colesterol
edad = st.slider('Edad', min_value=25, max_value=80, value=55, step=1)
colesterol = st.slider('Colesterol', min_value=120, max_value=600, value=242, step=2)

# Normalizar los valores con el scaler previamente entrenado
inputs = np.array([[edad, colesterol]])
inputs_scaled = scaler.transform(inputs)

# Realizar la predicción
prediccion = model.predict(inputs_scaled)

# Mostrar la predicción y las imágenes correspondientes
if prediccion == 0:
    st.image('https://img.freepik.com/foto-gratis/feliz-mujer-atractiva-bailando-divirtiendose-levantando-manos-preocupaciones-disfrutando-musica-pie-contra-pared-blanca_176420-38816.jpg?semt=ais_hybrid&w=740&q=80', use_column_width=True)
    st.write("**¡Estás libre de problemas cardíacos!** 😄")
else:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzZ-b0TiMIFhmvLWtPJSM0LPct4ODjQEhlww&s', use_column_width=True)
    st.write("**Alerta de posibles problemas cardíacos. Consulta a un médico.** ⚠️")

# Mostrar los valores de entrada
st.write(f"Valores ingresados: Edad = {edad} años, Colesterol = {colesterol} mg/dl")

