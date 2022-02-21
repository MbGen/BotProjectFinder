from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
import aiogram.utils.markdown as fmt
from models.project import Project
from models.project_obj import ProjectCreator


creator_project_callback = inline.callback_data.ProfileCallback.MY_PROJ_CREATOR
searcher_project_callback = inline.callback_data.ProfileCallback.MY_PROJ_SEARCHER

edit_project_kb = inline.callbacks.ProfileKB.get_edit_project_kb()


@dp.callback_query_handler(lambda call: call.data == creator_project_callback)
async def get_creator_project(callback_query: types.CallbackQuery) -> None:
    try:
        instance = ProjectCreator(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, instance, reply_markup=edit_project_kb)
    except Project.DoesNotExist:
        await bot.send_message(callback_query.from_user.id, "Проекта нет, можете его создать в своем профиле")
