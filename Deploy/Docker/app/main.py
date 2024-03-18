import pickle
import uvicorn
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

# Inicia API
app = FastAPI()

# Carrega modelo
with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Cria página inicial
@app.get("/")
def home():
    return "Welcome to the Medical Insurence Prediction app!"

# Classifica custo médico (consumo do modelo)
@app.get('/predict')
def predict(age: int, bmi: float, children: int, smoker: str='no'):
    df_input = pd.DataFrame(dict(age=age, bmi=bmi, children=children, smoker=smoker), index=[0])
    prediction = model.predict(df_input)[0]
    output = prediction
    return output

# Classifica custo médico (consumo do modelo) com input no formato Json
class Customer(BaseModel):
    age: int
    bmi: float
    children: int
    smoker: str
    # Exemplo de uso:
    class Config:
        schema_extra = {
            "example": {
                "age": 20,
                "bmi": 30.4,
                "children": 1,
                "smoker": "yes",
            }
        }

@app.post('/predict_with_json')
def predict(data: Customer):
    df_input = pd.DataFrame(data.dict(), index=[0])
    prediction = model.predict(df_input)[0]
    return prediction


# Classifica custo médico (consumo do modelo) com input no formato Json - lista
class CustomerList(BaseModel):
    data: List[Customer]


@app.post('/mult_predict_with_json')
def predict(data: CustomerList):
    df_input = pd.DataFrame(data.dict()['data'])
    prediction = model.predict(df_input).tolist()
    return prediction
