from loader import dp
from aiogram import types, filters
from keyboards import inline
from keyboards.inline.callback_data import MenuCallback

keyboard_menu = inline.callbacks.MenuKB.get_menu_kb()


@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands=["menu"])
async def main_menu(msg: types.Message) -> None:
    await msg.answer("Вот что вы можете сделать", reply_markup=keyboard_menu)
