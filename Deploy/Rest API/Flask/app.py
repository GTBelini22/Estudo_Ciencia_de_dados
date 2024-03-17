import pickle
import pandas as pd
from flask import Flask
from flask_restful import Resource, Api 


app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return 'Bem vindo ao modelo de predição de seguros médicos API'


if __name__ == '__main__':
    app.run()