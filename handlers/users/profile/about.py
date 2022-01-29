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
                           fmt.text(
                               fmt.code("Ваш никнейм - ", user_cursor.nickname),
                               fmt.code("Ваш возраст - ", user_cursor.age),
                               fmt.code("Ваша выбранная тема - ", user_cursor.theme),
                               fmt.code(f"Что вы умеете - ", user_cursor.skills),
                               fmt.code(f"О вас - ",
                                        user_cursor.about if user_cursor.about else 'Вы ничего о себе не писали'),
                               sep="\n"
                           )
                           )
