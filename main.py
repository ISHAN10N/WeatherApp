import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city = input("enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=40fe4e47cb1c437599f40522231708&q={city}"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
speak.Speak(f'The current weather in {city} is {w}degree')
