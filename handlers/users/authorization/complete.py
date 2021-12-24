from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.user.authorization import Authorization
from keyboards import inline
from models.user import User


callback_searcher_chosen = inline.callback_data.CallbackData.SEARCHER
callback_creator_chosen = inline.callback_data.CallbackData.CREATOR


@dp.callback_query_handler(text_contains=callback_searcher_chosen)
async def user_type_searcher(callback_query: types.CallbackQuery) -> None:
    user_cursor = User.get(User.id == callback_query.from_user.id)
    user_cursor.type_of_user = 0
    user_cursor.save()
    # TODO: добавить в БД тип юзера
    await bot.send_message(callback_query.from_user.id, "Вы успешно закончили регистрацию")
    pass


@dp.callback_query_handler(text_contains=callback_creator_chosen)
async def user_type_searcher(callback_query: types.CallbackQuery) -> None:
    # TODO: добавить в БД тип юзера
    user_cursor = User.get(User.id == callback_query.from_user.id)
    user_cursor.type_of_user = 1
    user_cursor.save()
    await bot.send_message(callback_query.from_user.id, "Вы успешно закончили регистрацию")
    pass
