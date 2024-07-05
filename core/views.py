from django.shortcuts import render
import requests
import os

api_key = os.getenv("API_KEY")

def index(request):
    if(request.POST):
        cities = request.POST.dict()
        data = cities.get('cities')
        print(api_key)
        if data:
            try:
                link = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={api_key}"
                dados = requests.get(link)
                weather = dados.json()
                print(weather)
                description = weather['weather'][0]['description']
                print(description)
                icon = weather['weather'][0]['icon']
                print(icon)
                temperatura = weather['main']['temp']
                calor = celsius(temperatura)
                print(calor)
                nome = weather['name']
                umidade = weather['main']['humidity']
                print(nome)
                content = {
                    "descricao": description,
                    "icon": icon,
                    "nome": nome,
                    "calor": calor,
                    "umidade": umidade
                }
            except:
                print("Erro")
        else:
            content={
                    "descricao": "Sem Descricao",
                    "icon": " ",
                    "nome": " ",
                    "calor": "0",
                    "umidade": "0"      
                }
            return render(request, "index.html",content)
    return render(request, "index.html", content)

def celsius(temperatura):
    ts = temperatura - 273
    formar = int(ts)
    return f"A Temperatura atual é de {formar} ºC"
