from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization


@dp.message_handler(state=Authorization.waiting_for_type_of_user)
async def get_type_of_user(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(type_of_user=msg.text)
    print(await state.get_data())
    await state.finish()
