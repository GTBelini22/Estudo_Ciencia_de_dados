import pickle
import pandas as pd
from flask import Flask , request
from flask_restful import Resource, Api 


app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return 'Bem vindo ao modelo de predição de seguros médicos API'



@app.route('/predict', methods=['POST'])

def index():
    data_json = request.get_json()['data']
    
    # Criando um dataframe
    df = pd.DataFrame(data_json)
    
    # Carregando o modelo
    with open('models/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
        
    # A saida precisa ser alterada, um dataframe da errado na hora de sair
    # Predições
    output = model.predict(df).tolist()
    return output
    
    


if __name__ == '__main__':
    app.run()