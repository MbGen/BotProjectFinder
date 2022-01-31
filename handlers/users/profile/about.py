from loader import dp, bot
from aiogram import types, filters
import aiogram.utils.markdown as fmt
from keyboards import inline
from keyboards.inline.callback_data import ProfileCallback
from models.user import User


@dp.callback_query_handler(text_contains=ProfileCallback.ABOUT_ME)
async def about_me(callback_query: types.CallbackQuery) -> None:
    user_cursor = User.get(id=callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id,
                           f"<strong>Ваш никнейм</strong> - <em>{user_cursor.nickname}</em>\n"
                           f"<strong>Ваш возраст</strong> - <em>{user_cursor.age}</em>\n"
                           f"<strong>Ваша выбранная тема</strong> - <em>{user_cursor.theme}</em>\n"
                           f"<strong>Что вы умеете</strong> - <em>{user_cursor.skills}</em>\n"
                           f"О вас - {user_cursor.about if user_cursor.about else 'Вы ничего о себе не писали'}"
                           )
