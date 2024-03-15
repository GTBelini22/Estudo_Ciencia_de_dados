import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title = "Predição de seguro de saúde",
    page_icon = "img\stethoscope.png"
)
st.sidebar.header('Calcular o Seguro')

# Titulo da página
st.title('Predição de seguro de saúde')

st.markdown("Predição do seguro de saúde a partir das seguintes métricas:")
