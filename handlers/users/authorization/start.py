from aiogram import types, filters
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards import inline


keyboard_auth = inline.callbacks.AuthorizationKB.get_authorize_kb()


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE), state='*')
async def bot_start(msg: types.Message, state: FSMContext) -> None:
    User.get_or_create(id=msg.from_user.id)
    await state.finish()
    await msg.answer(f"👋 Привет, {msg.from_user.first_name}", reply_markup=keyboard_auth)
