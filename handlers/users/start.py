from aiogram import types, filters
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp, bot
from .. import states


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def bot_start(msg: types.Message):
    User.get_or_create(id=msg.from_user.id)
    await msg.answer('''
👋 Привет, {} 
'''.format(msg.from_user.first_name))


async def get_user_info():
    pass

