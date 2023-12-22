import requests
#import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

ac = 0.0
dc = 0.1
volts = 0.2
potencia = (volts*dc)
energia_gerada = 0.4

corrente = {}
corrente['alternada'] = ac
corrente['continua'] = dc
corrente['potencia'] = potencia
corrente['totalGerado'] = energia_gerada


API_KEY = "1cc137a0815ef8cc3f20971c0e9646b4"
cidade = 'feira de santana'
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"



requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura}ºC")

# construir funcionalidades
@app.route('/')
def homepage():
    return 'a api esta no ar'

@app.route("/clima")
def retornaclima():
    return requisicao.json()

@app.route('/corrente')
def retornarCorrenteContinua():
    return jsonify(corrente)

#@app.route('/potencia')
#def retornarPotenciaAtual():
#    return .json()

#@app.route('/totalgerado')
#def retornarTotalGerado():
#    return energia_gerada.json()



#roda a api
app.run(host='0.0.0.0')