import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4')


@bot.message_handler(commands=['start'])
def news(message):
    bot.send_message(message.chat.id, 'введите хештег')
    faf()


def faf(message):
    msg1 = bot.send_message(message.chat.id,)
    tekst = message.text
    bot.register_next_step_handler(msg1, tekst)
	

bot.infinity_polling()