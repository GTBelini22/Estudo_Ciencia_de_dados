import pandas as pd
import requests
import json

url = 'http://localhost:5000/predict'


# Inserindo os dados de entrada
df_input = pd.DataFrame({
    'age': [60, 21, 24],
    'bmi': [36.005, 21.89, 29.83],
    'children': [0, 2, 0],
    'smoker': ['no', 'yes', 'no']
})

# Colocado no formato json para ser lido
json_input = {'data':df_input.to_dict(orient='records')}

resposta = requests.post(url,json=json_input)

# Se for 200 é que deu certo
print(resposta)

print(resposta.json())

