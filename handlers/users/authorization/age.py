from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from utils.validation.data_validation import Validator
from keyboards.inline.callbacks import AuthorizationKB
from models.user import User


@dp.message_handler(state=Authorization.waiting_for_age)
async def get_age(msg: types.Message, state: FSMContext) -> None:
    if Validator.is_valid_age(msg.text):
        user_cursor = User.get(User.id == msg.from_user.id) 
        user_cursor.age = msg.text 
        user_cursor.save()
        await state.finish()
        await msg.answer(f"Отлично, теперь выберите интересующую вас тему",
                         reply_markup=AuthorizationKB.get_choice_theme_kb())
    else:
        await msg.answer("Возраст меньше чем 0, или больше 100, введите коректный")
        await Authorization.waiting_for_age.set()
