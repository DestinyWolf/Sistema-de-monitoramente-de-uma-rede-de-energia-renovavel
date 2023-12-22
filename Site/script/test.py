import requests
from os import system as sys

link = 'http://localhost:3000/clima'
link2 = 'http://localhost:3000/dados'



requisicao = requests.get(link)
requisicao2 = requests.get(link2)

dados = requisicao.json()
dados2 = requisicao2.json()
sys('cls')
#print(requisicao)
#print(dados)
print(f"cidade: {dados['name']}\ntemperatura: {(dados['main']['temp'] - 273):.2f}\nvelocidade do vento: {(dados['wind']['speed'] * 3.6)}km/h\n")
#print(requisicao2, "\n")

#print(dados2)
print(f"corrente continua: {dados2['continua']}\ncorrente alternada: {dados2['alternada']}\namperagem: {dados2['amp']}\npotencia: {dados2['potencia']}\ntotal gerado: {dados2['totalGerado']}")