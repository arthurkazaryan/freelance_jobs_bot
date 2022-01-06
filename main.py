import os
import telebot
from time import sleep
import datetime
from random import randint
from pytz import timezone
from dotenv import load_dotenv, find_dotenv
from upwork.parse import prepare_message

load_dotenv(find_dotenv())
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    while True:
        current_time = datetime.datetime.now().astimezone(timezone("Europe/Moscow"))
        if current_time.hour in range(12, 24):
            new_messages = prepare_message()
            if new_messages:
                for msg in new_messages:
                    bot.send_message(message.chat.id, msg)
        sleep(randint(177, 325))


bot.polling()
