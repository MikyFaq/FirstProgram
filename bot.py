#import PYOWM and TELEBOT
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
#Telebot key for bot
bot = telebot.TeleBot("1961035872:AAG-e4IZSFIt5jVXtrHkGouEejPRzNsla9M")
#PyOWM key for weather
owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'
#Start bot message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите город/страну:")
#all bot message
@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        #get info about weather
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        #about temperature
        temp = w.temperature('celsius')["temp"]
        answer = "В городе/стране " + message.text + " сейчас " + w.detailed_status + "\n"
        answer += "Температура сейчас:" + str(temp) + "°" +  "\n\n"
        #советы
        if temp <= 10:
            answer += "Холодновато, одевайся потеплее"
        elif temp <= 20:
            answer += "Прохладно, лучше одеться потеплее."
        else:
            answer += "Тепло, одевай что хочешь."
        bot.send_message(message.chat.id, answer)
    except:
        #warning
        bot.send_message(message.chat.id, 'Ошибка! Город/Страна не найден(а). Напиши /start.')
bot.polling(none_stop=True)
