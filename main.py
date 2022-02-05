import logging
import aiogram

# токен бота
TOKEN = '1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4'


# создание бота
bot = aiogram.Bot(token="1742310134:AAE_szafX_AUqtECbgVIr0u-OVyKbXSE8J4")


dp = aiogram.Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: aiogram.types.Message):
    await message.reply("Test 1")


if __name__ == "__main__":
    # Запуск бота
    aiogram.executor.start_polling(dp, skip_updates=True)