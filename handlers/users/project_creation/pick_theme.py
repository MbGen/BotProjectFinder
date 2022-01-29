from loader import dp, bot
from aiogram import types
from keyboards import inline
from models.project import Project
from states.user.add_project import ProjectAdd


bots_chosen = inline.callback_data.ThemeCreateCallback.CREATE_BOTS
web_chosen = inline.callback_data.ThemeCreateCallback.CREATE_WEB


@dp.callback_query_handler(text_contains=bots_chosen)
async def bots_theme(callback_query: types.CallbackQuery) -> None:
    project_cursor = Project.get(Project.id == callback_query.from_user.id)
    project_cursor.theme = bots_chosen
    project_cursor.save()
    await bot.send_message(callback_query.from_user.id, "А теперь опишите ваш проект")
    await ProjectAdd.waiting_for_description.set()


@dp.callback_query_handler(text_contains=web_chosen)
async def web_theme(callback_query: types.CallbackQuery) -> None:
    project_cursor = Project.get(Project.id == callback_query.from_user.id)
    project_cursor.theme = web_chosen
    project_cursor.save()
    await bot.send_message(callback_query.from_user.id, "А теперь опишите ваш проект")
    await ProjectAdd.waiting_for_description.set()
