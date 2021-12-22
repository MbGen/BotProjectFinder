from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization


@dp.message_handler(state=Authorization.waiting_for_age)
async def get_age(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь выберите интересующую вас тему")
    await state.update_data(age=msg.text)
    # TODO: добавить кнопки с темами
    await Authorization.waiting_for_theme.set()
