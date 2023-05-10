import random
import telebot
from telebot import types

# Введите токен вашего бота здесь
TOKEN = '6264189747:AAHNnlUT4JhM-W_JEnzRNKKXEqIOE4mBNfM'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Определяем текст сообщения
def generate_message():
    assets = ['Crypto IDX']
    times = ['1 minute', '2 minutes', '3 minutes', '4 minutes', '5 minutes']
    signals = ['UP (Green Button)', 'DOWN (Red Button)']
    message = 'Asset - {}, Time - {}, Signal - {}'.format(random.choice(assets), random.choice(times), random.choice(signals))
    return message

# Определяем кнопку и обработчик нажатия
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Get New Signal')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Press the button to get a new signal", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Get New Signal':
        bot.send_message(message.chat.id, generate_message())

# Запускаем бота
bot.polling()
