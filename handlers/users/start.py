from aiogram import types, filters
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from models.user import User
from loader import dp, bot
from keyboards import inline
from states.user.authorization import Authorization

# TODO: валидировать введенные данные, и добавить их в БД

callback_auth = inline.callback_data.CallbackDataEnum.AUTHORIZATION.value
keyboard_auth = inline.callbacks.Authorization.authorize_kb()


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def bot_start(msg: types.Message) -> None:
    User.get_or_create(id=msg.from_user.id)
    await msg.answer(f"👋 Привет, {msg.from_user.first_name}", reply_markup=keyboard_auth)


@dp.callback_query_handler(lambda callback: callback.data == callback_auth)
async def start_getting_user_description(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(callback_query.from_user.id, "Напишите свой ник")
    await Authorization.waiting_for_nickname.set()


@dp.message_handler(state=Authorization.waiting_for_nickname)
async def get_nickname(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь ваш возраст (можете соврать)")
    await state.update_data(nickname=msg.text)
    await Authorization.waiting_for_age.set()


@dp.message_handler(state=Authorization.waiting_for_age)
async def get_age(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь выберите интересующую вас тему")
    await state.update_data(age=msg.text)
    # TODO: добавить кнопки с темами
    await Authorization.waiting_for_theme.set()


@dp.message_handler(state=Authorization.waiting_for_theme)
async def get_theme(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь напишите что вы умеете")
    await state.update_data(theme=msg.text)
    await Authorization.waiting_for_skills.set()


@dp.message_handler(state=Authorization.waiting_for_skills)
async def get_skills(msg: types.Message, state: FSMContext) -> None:
    await msg.answer(f"Отлично, теперь расскажите кратко о себе (Не объязательно)")
    await state.update_data(skills=msg.text)
    await Authorization.waiting_for_about.set()


@dp.message_handler(state=Authorization.waiting_for_about)
async def get_about(msg: types.Message, state: FSMContext) -> None:
    await msg.answer("Отлично, теперь выберите вы будете искать проект, или его создавать")
    await state.update_data(about=msg.text)
    # TODO: добавить кнопки с выбором типа юзера
    await Authorization.waiting_for_type_of_user.set()


@dp.message_handler(state=Authorization.waiting_for_type_of_user)
async def get_type_of_user(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(type_of_user=msg.text)
    print(await state.get_data())
    await state.finish()
