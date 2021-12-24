from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from keyboards.inline.callbacks import AuthorizationKB


@dp.message_handler(state=Authorization.waiting_for_about)
async def get_about(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(about=msg.text)
    await msg.answer("Отлично, теперь выберите вы будете искать проект, или его создавать",
                     reply_markup=AuthorizationKB.choice_type_of_user())
    # TODO: добавить в БД state.get_data()
    await state.finish()
