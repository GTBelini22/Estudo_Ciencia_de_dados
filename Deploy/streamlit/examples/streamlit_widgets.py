import streamlit as st

st.set_page_config(page_title='DNC')

st.write('Hello world')

# Elementos de texto
st.title('Pagina Inicial')
st.markdown("Aqui um texto ***usando*** [markDown](https://www.markdownguide.org/)")


# Texto na lateral
st.sidebar.header('Texto na lateral')

# Widgets
var_strNome = st.text_input('Qual o seu nome')
st.write(f'Muito prazer {var_strNome}')

# Numeros - value é o valor padrão
var_intIdade =  st.number_input('Qual a sua idade?', value=18)
st.write(f'Você tem {var_intIdade} anos')

# Widgets página lateral
super_poder =  ['Jedi', 'Bilionario', 'Super MAN']
var_superPoder = st.sidebar.selectbox('Qual o seu super poder? ',options=super_poder)
st.sidebar.write(f'O seu super poder é {var_superPoder}')
