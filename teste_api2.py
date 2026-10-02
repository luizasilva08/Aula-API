#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UMA CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA

import requests #biblioteca para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir os dados de forma legível

cidade = str(input("Insira a cidade que você quer ver: "))
#VAMOS PRECISAR DA APIKEY -> UMA CREDENCIAL

API_LINK = "http://api.weatherapi.com/v1/astronomy.json"

parametros ={
    "key":API_KEY,
    "q": cidade, #cidade para qual queremos obter os dados
    "lang":"pt", #linguagem
}

#ARMAZENANDO A RESPOSTA DA REQUISIÇÃO NA VARIÁVEL RESPOSTA

resposta = requests.get(API_LINK, params=parametros)

#print(resposta)
#status code: 200 (sucesso) ou 401(erro)

#print(resposta.content)

if resposta.status_code == 200:
    print("\033[034mRequisição realizada com sucesso!\033[m")
    dados = resposta.json() #armazenando os dados em formato json na variável dados
    #pprint(dados) #.json() bonitinho
    fase_da_lua = dados["astronomy"]["astro"]["moon_phase"] 
    print(f"A fase da lua no momento é {fase_da_lua}")
    crepusculo = dados["astronomy"]["astro"]["sunset"] 
    print(f"O pôr-do-sol aconteceu {crepusculo}")

else:
    print("\033[031mErro na requisição.\033[m")


