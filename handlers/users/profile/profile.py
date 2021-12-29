from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
from keyboards.inline.callback_data import MenuCallback


keyboard_profile = inline.callbacks.MenuKB.get_profile_kb()


@dp.callback_query_handler(text_contains=MenuCallback.PROFILE)
async def profile(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.edit_text(text="Ваш профиль", reply_markup=keyboard_profile)
