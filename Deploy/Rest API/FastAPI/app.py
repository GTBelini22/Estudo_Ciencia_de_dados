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


@app.get('/predict')
def predict(age:int, bmi:float, children:int, smoker:str = 'no'):
    df_input = pd.DataFrame([dict(age=age, bmi=bmi, children= children, smoker=smoker)])
    output = model.predict(df_input)[0]
    return output


if __name__ == '__main__':
    uvicorn.run(app)