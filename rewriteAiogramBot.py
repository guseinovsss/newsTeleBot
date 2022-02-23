import logging
import aiogram
from bs4 import BeautifulSoup
import requests



# токен бота
TOKEN = '1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4'


# создание бота
bot = aiogram.Bot(token="1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4")


dp = aiogram.Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands=["ria"])
async def cmd_test1(message: aiogram.types.Message):
    URL = 'https://ria.ru/world'
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'# юзер агент
    }

    response = requests.get(URL, headers = HEADERS)



if __name__ == "__main__":
    # Запуск бота
    aiogram.executor.start_polling(dp, skip_updates=True)