from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
from keyboards.inline.callback_data import MenuCallback
from typing import Union


keyboard_menu = inline.callbacks.MenuKB.get_menu_kb()


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands=["menu"])
async def main_menu(msg: types.Message) -> None:
    await msg.answer("Вот что вы можете сделать", reply_markup=keyboard_menu)


@dp.callback_query_handler(text_contains=MenuCallback.MAIN_MENU)
async def main_menu_callback(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.edit_text(text="Вот что вы можете сделать", reply_markup=keyboard_menu)
