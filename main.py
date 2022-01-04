import os
import telebot
import time
from dotenv import load_dotenv, find_dotenv
from upwork.parse import prepare_message

load_dotenv(find_dotenv())
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, 'Hey!')


@bot.message_handler(commands=['start'])
def hello(message):
    while True:
        new_messages = prepare_message()
        if new_messages:
            for msg in new_messages:
                bot.send_message(message.chat.id, msg)
        time.sleep(300)


bot.polling()
