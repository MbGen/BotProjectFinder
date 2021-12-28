from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
from keyboards.inline.callback_data import MenuCallback


keyboard_profile = inline.callbacks.MenuKB.get_profile_kb()


@dp.callback_query_handler(text_contains=MenuCallback.PROFILE)
async def profile(callback_query: types.CallbackQuery) -> None:
    # TODO: Вместо новго сообщения, изменять старое
    await bot.send_message(callback_query.from_user.id, "Ваш профиль", reply_markup=keyboard_profile)
