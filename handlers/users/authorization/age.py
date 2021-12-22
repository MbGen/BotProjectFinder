from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization


@dp.message_handler(state=Authorization.waiting_for_nickname)
async def get_nickname(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь ваш возраст (можете соврать)")
    await state.update_data(nickname=msg.text)
    await Authorization.waiting_for_age.set()
