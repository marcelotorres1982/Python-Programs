import requests
import json
import pyttsx3

city = input(
    "Digite a cidade para a qual deseja obter informações meteorológicas: ")

# Faça uma solicitação à API OpenWeatherMap para obter as informações meteorológicas da cidade especificada
# gere a api aqui www.openweathermap.org
api_key = "4c32827255df476c9b975fd1966af90e"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(weather_url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Se a solicitação foi bem-sucedida, analise os dados JSON
    weather_data = json.loads(response.text)
    main_data = weather_data["main"]
    temperature_kelvin = main_data["temp"]
    temperature_celsius = temperature_kelvin - 273.15
    print(f"A temperatura em {city} é de {temperature_celsius:.0f}°C")

    engine = pyttsx3.init()
    engine.say(f"A temperatura em {city} é de {temperature_celsius:.0f}°C")
    engine.runAndWait()
else:
    # Se a solicitação não for bem-sucedida, imprima uma mensagem de erro
    print("Ocorreu um erro ao obter as informações meteorológicas.")
    engine = pyttsx3.init()
    engine.say("Ocorreu um erro ao obter as informações meteorológicas.")
    engine.runAndWait()