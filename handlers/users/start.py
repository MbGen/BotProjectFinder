from aiogram import types, filters
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp, bot
# TODO: разобраться с импортами
# cannot import name 'keyboards' from partially initialized module 'handlers' (most likely due to a circular import)


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def bot_start(msg: types.Message) -> None:
    User.get_or_create(id=msg.from_user.id)
    await msg.answer('''
👋 Привет, {} 
'''.format(msg.from_user.first_name))


@dp.callback_query_handler(func=lambda callback: callback.data == CallbackDataEnum.AUTHORIZATION.value)
async def start_info_handler(callback_query: types.CallbackQuery) -> None:
    await callback_query.answer("Вы желаете зарегестрироваться!")
