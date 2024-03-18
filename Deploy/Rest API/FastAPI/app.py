import pickle
import uvicorn
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


# Iniciando o API
app = FastAPI()

# Carregando modelo
with open('models/model.pkl', 'rb') as model_file:
    model =  pickle.load(model_file)
    
#Criando a pagina inicial
@app.get('/')
def home():
    return "Bem vindo ao modelo de predição de seguro de saúde"


@app.get('/predict')
def predict(age:int, bmi:float, children:int, smoker:str = 'no'):
    df_input = pd.DataFrame([dict(age=age, bmi=bmi, children= children, smoker=smoker)])
    output = model.predict(df_input)[0]
    return output

class Customer(BaseModel):
    age: int
    bmi: float
    children: int
    smoker: str
    class Config:
        schema_extra = {
            'example': {
                'age': 20,
                'bmi': 30.4,
                'children': 1,
                'smoker': 'no'
            }
        }

@app.post('/predict_with_json')
def predict(data: Customer):
    df_input = pd.DataFrame([data.dict()])
    output = model.predict(df_input)[0]
    return output

# Lista de clientes - previsão para varios clientes
class CustomerList(BaseModel):
    data: List[Customer]
    
@app.post('/predict_with_json_list')
def predict(data: CustomerList):
    df_input = pd.DataFrame(data.dict()['data'])
    output = model.predict(df_input).tolist()
    return output


if __name__ == '__main__':
    uvicorn.run(app)