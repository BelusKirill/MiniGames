from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import load_config

# Загрузка параметров для подключения
# Создание Dispatcher телеграмм бота
config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) 