from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization


@dp.message_handler(state=Authorization.waiting_for_theme)
async def get_theme(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь напишите что вы умеете")
    await state.update_data(theme=msg.text)
    await Authorization.waiting_for_skills.set()
