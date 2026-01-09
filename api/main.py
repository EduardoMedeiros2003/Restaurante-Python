from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação
    Docstring para hello_world
    '''

    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    Docstring para get_restaurantes
    :param restaurante: Descrição
    :type restaurante: str
    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    #O get vai solicitar a informação
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json() #Colocando os dados json na variavel dados_json
        if restaurante is None:# Se nada for encontrado faça isso, mostrar todos os restaurantes
            return{'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return{'Restaurante':restaurante, 'Cardapio': dados_restaurante}
         #Criando um dicionario com as informações
    else:
        return {f'Erro:{response.status_code} - {response.text}'}
