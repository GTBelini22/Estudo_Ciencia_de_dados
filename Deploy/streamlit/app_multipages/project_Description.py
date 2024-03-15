import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = "Predição de seguro de saúde",
    page_icon = "img\stethoscope.png"
)

st.sidebar.header('Descrição do porjeto')

st.write('# Bem vindo ao Predição de seguro de saúde🩺')
st.write('\n\n')

st.image('img\health_insurance_img.jpg')
st.write('\n\n')



st.markdown(
    """
        A previsão de seguro médico é crucial na área da saúde, pois prevê os custos médicos e auxilia as organizações de saúde a se prepararem para despesas. Ao analisar fatores como demografia, histórico médico e estilo de vida, as empresas de seguros podem definir taxas de prêmio precisas e alocar recursos de forma eficaz. Isso também ajuda pessoas de alto risco a receberem os recursos e apoio necessários. No geral, a previsão de seguro médico é uma ferramenta valiosa tanto para pacientes quanto para provedores em um sistema de saúde sustentável.

        Este aplicativo tem como objetivo prever o custo do seguro usando características de entrada como:

        - Idade
        - IMC
        - Número de filhos
        - Status de fumante
    """
)

st.success('Por favor, **vá para as próximas páginas** para realizar a predição')