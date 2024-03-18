import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI


# Iniciando o API
app = FastAPI()

# Carregando modelo
with open('models/model.pkl', 'rb') as model_file:
    model =  pickle.load(model_file)
    
#Criando a pagina inicial
@app.get('/')
def home():
    return "Bem vindo ao modelo de predição de seguro de saúde"


if __name__ == '__main__':
    uvicorn.run(app)