from loader import dp, bot
from aiogram import types, filters
from models.user import User
from models.project import Project
from models.project_obj import ProjectSearcher
from keyboards import inline
from utils.misc.logging import logger


navigation_kb = inline.callbacks.ProjectSearchKB.get_navigation_kb
find_project_callback = inline.callback_data.MenuCallback.FIND_PROJECT


# TODO: При возможности сделать по другому
async def get_theme(user_id: str) -> str:
    user_cursor = User.get(User.id == user_id)
    if "бот" in user_cursor.theme:
        return "проект о ботах"
    elif "веб" in user_cursor.theme:
        return "проект о вебе"


@dp.callback_query_handler(lambda call: call.data == find_project_callback)
async def find_project(callback_query: types.CallbackQuery) -> None:
    theme = await get_theme(callback_query.from_user.id)
    searcher = ProjectSearcher(theme)
    await bot.send_message(callback_query.from_user.id, searcher.get_next_project(), reply_markup=await navigation_kb())
