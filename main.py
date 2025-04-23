from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import logging
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен загружен
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден. Убедитесь, что файл .env существует и содержит BOT_TOKEN.")

# Создание бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="💼 Открыть Гения Инвестиций",
            web_app=WebAppInfo(url="https://genius-investor.vercel.app")
        )
    )
    await message.answer("Добро пожаловать в Гения Инвестиций! Жми кнопку ниже, чтобы начать:", reply_markup=keyboard)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
