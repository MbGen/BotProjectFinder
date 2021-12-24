from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from .user_info import USER_INFO


@dp.message_handler(state=Authorization.waiting_for_skills)
async def get_skills(msg: types.Message) -> None:
    USER_INFO.update(skills=msg.text)
    await msg.answer(f"Отлично, теперь расскажите кратко о себе (Не объязательно)")
    await Authorization.waiting_for_about.set()
