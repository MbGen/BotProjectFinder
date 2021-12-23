from aiogram import types, filters
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp
from keyboards import inline

keyboard_auth = inline.callbacks.AuthorizationKB.authorize_kb()


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def bot_start(msg: types.Message) -> None:
    User.get_or_create(id=msg.from_user.id)
    await msg.answer(f"👋 Привет, {msg.from_user.first_name}", reply_markup=keyboard_auth)
