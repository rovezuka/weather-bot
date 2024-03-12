import telebot
import requests
import json

bot = telebot.TeleBot('6879855900:AAHuGrNf1nTpcXB9b35T_pG6tNRnGSXYoo0')
API = 'd93ac610bc558a557c16e4c79c3c7bb1' # api с OpenWeather

@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(content_types=['text']) # если пользователь отправит текст
def get_weather(message):
        city = message.text.strip().lower() # сохранить город пользователя
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if res.status_code == 200: # успешно отправили запрос
                data = json.loads(res.text) # преобразовать в json-объект
                temp = data["main"]["temp"]
                bot.reply_to(message, f'Сейчас погода: {temp}') # выводим текущую погоду
                
                image = 'sunny.png' if temp > 5.0 else 'sun.png' # подставляем картинку в зависимости от температуры
                file = open('./' + image, 'rb') # открываем фото
                bot.send_photo(message.chat.id, file) # отправляем фото
        else:
                bot.reply_to(message, 'Город указан неверно') 


bot.polling(none_stop=True)