#импорт библиотек
import telebot
from bs4 import BeautifulSoup
import requests
from telepot.loop import MessageLoop
import re

# токен теле бота
bot = telebot.TeleBot('1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4')



# @bot.message_handler(commands = ['r'])
# def news1(message):
# 	vah = message
#  	result = re.match(r'text*[^\n]', str(vah))
# 	bot.send_message(message.chat.id, vah)


@bot.message_handler(commands = ['ria'])#декоратор с помощью которого наш бот будет реагировать на команду
def news(message):
	URL = 'https://ria.ru/world'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'# юзер агент
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll('a', 'list-item__title')

	for i in range(len(texts[:-16]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')#отправляем гиперсылку пользователю


@bot.message_handler(commands = ['vottak'])#декоратор с помощью которого наш бот будет реагировать на команду
def news(message):
	URL = 'https://vot-tak.tv/novosti'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
	}
	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll('a', 'post_card_frame')
	
	for i in range(len(texts[:-12]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')


@bot.message_handler(commands = ['rbcTrends'])#декоратор с помощью которого наш бот будет реагировать на команду
def news(message):
	URL = 'https://trends.rbc.ru/trends/?utm_source=topline'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll("a","item__title")

	for i in range(len(texts[:4]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')


@bot.message_handler(commands = ['rbkNewspaper'])#декоратор с помощью которого наш бот будет реагировать на команду
def news(message):
	URL = 'https://www.rbc.ru/newspaper/?utm_source=topline'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll("a","newspaper-page__news")

	for i in range(len(texts[:4]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')

@bot.message_handler(commands = ['rbk'])#декоратор с помощью которого наш бот будет реагировать на команду
def news(message):
	URL = 'https://www.rbc.ru/'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll("a","main__feed__link js-yandex-counter")

	for i in range(len(texts[:4]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')

@bot.message_handler(commands = ['mailru'])#декоратор с помощью которого наш бот будет реагировать на команду
def news(message):
	URL = 'https://news.mail.ru/economics/'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll("a","newsitem__title link-holder")

	for i in range(len(texts[:4]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')


@bot.message_handler(commands=['/findforhashtag'])
def start_message(message):
    bot.send_message(message.chat.id, '', reply_markup=keyboard)


@bot.message_handler(commands=['start','back'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/resours','/byVIP')
    keyboard.row('/findforhashtag','/help')

    bot.send_message(message.chat.id, 'выбери сайт', reply_markup=keyboard)

@bot.message_handler(commands=['resours'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/rbk', '/mailru','/vottak')
    keyboard.row('/rbkNewspaper', '/ria','/rbcTrends')
    keyboard.row('/back')
    bot.send_message(message.chat.id, 'выбери сайт', reply_markup=keyboard)
    
@bot.message_handler(commands=['help'])
def start_message(message):

    bot.send_message(message.chat.id, '', reply_markup=keyboard)
# SAID is programmer


bot.polling(none_stop = True) 