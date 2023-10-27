import requests, json
from dotenv import load_dotenv
import os
load_dotenv(override=True)

API_KEY = os.environ['API_KEY']
city_name = "recife"

cities = ["rio de janeiro", "são paulo", "minas gerais", "recife", "amazonas", "curitiba", "rio grande do norte", "ceara"]

def celsius(temp):
    ts = temp - 273
    return f" A temperatura em Celsisus é {ts} °C"

while True:
    usuario = input("Digite o nome da cidade que deseja ? ")
    if usuario not in cities:
        print("Digite apenas as cidades que são na lista")
    else:
        try:
            link = f"https://api.openweathermap.org/data/2.5/weather?q={usuario}&appid={API_KEY}"
            requisicao = requests.get(link)
            dic = requisicao.json()
            descricao = dic['weather'][0]['description']
            temperatura = dic['main']['temp']
            cv = int(temperatura)

            cv_temp = celsius(cv)
            print(cv_temp)
            print(descricao)
            continua = input("Deseja continuar S/N: ")
            if(continua == 'S' or continua == 's'):
                continue
            elif(continua == "N" or continua == "n"):
                break
            else:
                print("Digite somente sim ou não")
        except:
            print("Nome da cidade não esta correto")









