from aiogram import types
from loader import dp, bot
from states.user.authorization import Authorization
from keyboards import inline, reply
from models.user import User

callback_searcher_chosen = inline.callback_data.TypeOfUserCallback.SEARCHER
callback_creator_chosen = inline.callback_data.TypeOfUserCallback.CREATOR

menu_keyboard = reply.reply_keyboards.MenuKB.get_menu_kb()


@dp.callback_query_handler(text_contains=callback_creator_chosen)
async def user_type_searcher(callback_query: types.CallbackQuery) -> None:
    user_cursor = User.get(User.id == callback_query.from_user.id)
    user_cursor.is_creator = True
    user_cursor.save()
    await bot.send_message(callback_query.from_user.id,
                           "Вы успешно закончили регистрацию можете открыть меню",
                           reply_markup=menu_keyboard
                           )


@dp.callback_query_handler(text_contains=callback_searcher_chosen)
async def user_type_searcher(callback_query: types.CallbackQuery) -> None:
    user_cursor = User.get(User.id == callback_query.from_user.id)
    user_cursor.is_creator = False
    user_cursor.save()
    await bot.send_message(callback_query.from_user.id,
                           "Вы успешно закончили регистрацию можете открыть меню",
                           reply_markup=menu_keyboard
                           )
