from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
from keyboards.inline.callback_data import ProfileCallback


@dp.callback_query_handler(text_contains=ProfileCallback.ABOUT_ME)
async def about_me(callback_query: types.CallbackQuery) -> None:\
    await bot.send_message(callback_query.from_user.id, text="Информация об юзере")
