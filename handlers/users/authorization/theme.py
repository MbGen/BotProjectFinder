from aiogram import types
from loader import dp, bot
from states.user.authorization import Authorization
from keyboards import inline
from models.user import User
from .user_info import UserInfo

callback_bots_chosen  = inline.callback_data.CallbackData.BOTS
callback_web_chosen = inline.callback_data.CallbackData.WEB


@dp.callback_query_handler(text_contains=callback_bots_chosen)
async def bots_theme(callback_query: types.CallbackQuery) -> None:
    UserInfo.USER_INFO.update(theme=callback_bots_chosen)
    await bot.send_message(callback_query.from_user.id,
                           f"Вы выбрали тему {callback_bots_chosen}, теперь напишите что вы умеете")
    await Authorization.waiting_for_skills.set()


@dp.callback_query_handler(text_contains=callback_web_chosen)
async def web_theme(callback_query: types.CallbackQuery) -> None:
    UserInfo.USER_INFO.update(theme=callback_web_chosen)
    await bot.send_message(callback_query.from_user.id,
                                f"Вы выбрали тему {callback_web_chosen}, теперь напишите что вы умеете")
    await Authorization.waiting_for_skills.set()
