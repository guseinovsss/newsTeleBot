# import telepot
# import telebot
# from telepot.loop import MessageLoop
# from bs4 import BeautifulSoup
# import requests

# bot1 = telebot.TeleBot('1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4')
# bot = telepot.Bot('1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4')

# def news(message):
# 	URL = 'https://news.mail.ru/economics/'
# 	HEADERS = {
# 		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
# 	}

# 	response = requests.get(URL, headers = HEADERS)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	texts = soup.findAll("a","newsitem__title link-holder")

# 	for i in range(len(texts[:4]), -1, -1):
# 		txt = str(i + 1) + ') ' + texts[i].text
# 		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')


# @bot1.message_handler(commands = ['onbot'])
# def handle(msg):
#     if msg['text'] == "start":
#         news()
	

# MessageLoop(bot,handle).run_as_thread()