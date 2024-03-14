import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(page_title='Insurance Prediction')

# Titulo da página
st.title('Insurance Prediction')


# Parametros
# Esses valores de máximos e minimo são referentes ao dataset que foi feita a analise 
var_age= st.number_input(label='Idade', value=18, min_value=18, max_value=120)
var_bmi = st.number_input(label='BMI', value=30.0)
var_children = st.slider(label='Número filhos', min_value=0, max_value=5)
var_smoker = st.selectbox(label='Fumante', options=['Sim', 'Não'])

# modelo de dados
