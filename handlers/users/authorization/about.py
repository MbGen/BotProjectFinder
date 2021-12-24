from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from keyboards.inline.callbacks import AuthorizationKB
from models.user import User


@dp.message_handler(state=Authorization.waiting_for_about)
async def get_about(msg: types.Message, state: FSMContext) -> None:
    user_cursor = User.get(User.id == msg.from_user.id) 
    user_cursor.about = msg.text 
    user_cursor.save()
    await state.update_data(about=msg.text)
    await msg.answer("Отлично, теперь выберите вы будете искать проект, или его создавать",
                     reply_markup=AuthorizationKB.choice_type_of_user())
    # TODO: добавить в БД state.get_data()
    await state.finish()
