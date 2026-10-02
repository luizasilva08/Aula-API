#UMA API É UM JEITO DE CONECTAR SISTEMAS, INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTES SISTEMAS
#DE SOFTWARE SE COMUNIQUEM E TROQUEM DADOS ENTRE SI;

#NESTE EXEMPLO, SERÁ UTILIZADA A *WEATHERapi.com* PARA CONSULTAR AS CONDIÇÕES
#CLIMÁTICAS DE UMA DETERMINADA LOCALIDADE;

#CONSUMIR API ->
#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UMA CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA

import requests #biblioteca para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir os dados de forma legível

pais = str(input("Insira o país que você quer ver a temperatura: "))
cidade = str(input("Insira a cidade que você quer ver a temperatura: "))
#VAMOS PRECISAR DA APIKEY -> UMA CREDENCIAL

API_LINK = "http://api.weatherapi.com/v1/current.json"

parametros ={
    "key":API_KEY,
    "q": cidade, #cidade para qual queremos obter os dados
    "lang":"pt", #linguagem
    "localtime":"2026-10-02 13:00", 
    "country": pais
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
    temperatura = dados["current"]["temp_c"] #armazenando a temp em °C
    descricao = dados["current"]["condition"]["text"] #armazenando a descrição
    print(f"A temperatura atual em {cidade} é de {temperatura} °C")
    print(f"Descrição do clima: {descricao}")




else:
    print("\033[031mErro na requisição.\033[m")


