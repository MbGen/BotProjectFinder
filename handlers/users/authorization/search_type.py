from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization


@dp.message_handler(state=Authorization.waiting_for_about)
async def get_about(msg: types.Message, state: FSMContext) -> None:
    await msg.answer("Отлично, теперь выберите вы будете искать проект, или его создавать")
    await state.update_data(about=msg.text)
    # TODO: добавить кнопки с выбором типа юзера
    await Authorization.waiting_for_type_of_user.set()
