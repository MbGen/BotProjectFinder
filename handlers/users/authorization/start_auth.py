from aiogram import types
from loader import dp, bot
from keyboards import inline
from states.user.authorization import Authorization


callback_auth = inline.callback_data.CallbackData.AUTHORIZATION


@dp.callback_query_handler(text_contains=callback_auth)
async def start_getting_user_description(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(callback_query.from_user.id, "Напишите свой ник")
    await Authorization.waiting_for_nickname.set()
