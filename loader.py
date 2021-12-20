from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('5087677967:AAHarKEs-_eLC5yuKGjSDbvbE0bwCi7kui0'), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
