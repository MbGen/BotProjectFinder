from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
from keyboards.inline.callback_data import MenuCallback
from models.user import User


creator_keyboard_profile = inline.callbacks.ProfileKB.get_creator_kb()
searcher_keyboard_profile = inline.callbacks.ProfileKB.get_searcher_kb()


@dp.callback_query_handler(text_contains=MenuCallback.PROFILE)
async def profile(callback_query: types.CallbackQuery) -> None:
    user_cursor = User.get(id=callback_query.from_user.id)

    if user_cursor.is_creator:
        await callback_query.message.edit_text(text="Ваш профиль", reply_markup=creator_keyboard_profile)
    else:
        await callback_query.message.edit_text(text="Ваш профиль", reply_markup=searcher_keyboard_profile)
