import os
import streamlit as st
import pandas as pd
import joblib

print(os.getcwd())

# Load the model
try:
    modelo = os.path.join('/03_PKL/m_tiempo_pedido_normal.pkl')
except Exception as e:
    st.error(f'Error loading model or encoders: {e}')


# Se inicia el título inicial de la app
st.title('Predicción de Tiempo de Pedido')

# Definir inputs
def obtener_inputs():
    inputs = {}
    # Añade aquí los inputs necesarios para tu modelo
    inputs['distancia'] = st.number_input('Distancia (km)', min_value=0.0, step=0.1)
    inputs['hora_dia'] = st.number_input('Hora del día', min_value=0, max_value=23)

    return pd.DataFrame([inputs])

# Botón de predicción
if st.button('Predecir Tiempo de Pedido'):
    datos = obtener_inputs()
    prediccion = modelo.predict(datos)
    st.success(f'Tiempo estimado: {prediccion[0]:.2f} minutos')

# Ejecutar la 