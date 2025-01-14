import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title = "Predição de seguro de saúde",
    page_icon = "img\stethoscope.png"
)
st.sidebar.header('Predição de Arquivo')

# Titulo da página
st.title('Predição de seguro de saúde usando um arquivo csv')

# -- model -- #
caminho_arq = r'C:\Users\gusta\OneDrive\Área de Trabalho\Cursos\DNC\Projetos\Estudo Ciencia de dados\Deploy\streamlit\models\model.pkl'
with open(caminho_arq, 'rb') as model_file:
    model =  pickle.load(model_file)
    

# Subindo os dados
data =  st.file_uploader('Upload do dataset')
if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction = insurance_prediction)
    
    st.markdown('Custo do plano de saúde:')
    st.write(df_output)
    st.download_button(label='Baixar CSV', data=df_output.to_csv(index=False),
                       mime='text/csv', file_name='Predicao_seguro.csv')
    
    
    
