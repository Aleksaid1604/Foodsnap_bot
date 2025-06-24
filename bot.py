import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Я — FoodSnap_AI_bot. Отправь фото еды, и я помогу посчитать калории.")

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer("/start — начать\n/help — помощь")

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    await message.answer("Фото получено! Распознавание скоро появится :)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
