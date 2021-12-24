from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from utils.validation.data_validation import Validator
from .user_info import USER_INFO


@dp.message_handler(state=Authorization.waiting_for_nickname)
async def get_nickname(msg: types.Message, state: FSMContext) -> None:
    if Validator.is_valid_nickname(msg.text):
        USER_INFO.update(nickname=msg.text)
        await msg.answer(f"Отлично, теперь ваш возраст (можете соврать)")
        await Authorization.waiting_for_age.set()
    else:
        await msg.answer("Никнейм занят, введите заново")
        await Authorization.waiting_for_nickname.set()
