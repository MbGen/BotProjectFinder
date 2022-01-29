from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from models.user import User


@dp.message_handler(state=Authorization.waiting_for_skills)
async def get_skills(msg: types.Message, state: FSMContext) -> None:
    user_cursor = User.get(User.id == msg.from_user.id) 
    user_cursor.skills = msg.text 
    user_cursor.save()
    await msg.answer(f"Отлично, теперь расскажите кратко о себе \(Не объязательно\)")
    await Authorization.waiting_for_about.set()
