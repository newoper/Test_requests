'''
-----------------------------------------------------------
 Прогноз погоды на Python за час (Яндек Практикум)
-----------------------------------------------------------

импорт библиотек requests и json
объявление переменной с городом — city
объявление переменной с адресом запроса — url
объявление переменной с самим запросом — weather_data
получение ответа и его преобразование в объект — requests.get.json()
объявление переменной с температурой — temperature
объявление переменной с ощущаемой температурой — temperature_feels
объявление переменной со скоростью ветра — wind-speed
вывод сообщениий о погоде — print('Сейчас в городе {город} {температура} градусов' и остальных.
-----------------------------------------------------------
Список АПИшок
https://apilist.fun/
'''



import requests
import json

city = 'Воронеж'

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
temperature_feels  = round(weather_data['main']['feels_like'])
wind_speed = round(weather_data['wind']['speed'])

print('Сейчас в городе', city, str(temperature), 'градусов')
print('Ощущается как',str(temperature_feels), 'градусов')
print('Скорость ветра',str(wind_speed), 'м/с')