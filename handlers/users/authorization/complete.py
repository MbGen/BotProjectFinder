from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from keyboards import inline
from .user_info import UserInfo
from models.user import User

callback_searcher_chosen = inline.callback_data.CallbackData.SEARCHER
callback_creator_chosen = inline.callback_data.CallbackData.CREATOR


@dp.callback_query_handler(text_contains=callback_searcher_chosen)
async def user_type_searcher(callback_query: types.CallbackQuery) -> None:
    UserInfo.USER_INFO.update(type_of_user=0)
    user_cursor = User(**USER_INFO)
    user_cursor.save()
    UserInfo.USER_INFO.clear()
    await bot.send_message(callback_query.from_user.id, "Вы успешно закончили регистрацию")


@dp.callback_query_handler(text_contains=callback_creator_chosen)
async def user_type_searcher(callback_query: types.CallbackQuery) -> None:
    UserInfo.USER_INFO.update(type_of_user=1)
    user_cursor = User(**USER_INFO)
    user_cursor.save()
    UserInfo.USER_INFO.clear()
    await bot.send_message(callback_query.from_user.id, "Вы успешно закончили регистрацию")
