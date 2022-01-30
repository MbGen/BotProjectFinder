from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
import aiogram.utils.markdown as fmt
from models.project import Project
from models.project_obj import ProjectCreator


creator_project_callback = inline.callback_data.ProfileCallback.MY_PROJ_CREATOR
searcher_project_callback = inline.callback_data.ProfileCallback.MY_PROJ_SEARCHER


@dp.callback_query_handler(text_contains=creator_project_callback)
async def get_creator_project(callback_query: types.CallbackQuery) -> None:
    project_cursor = Project.get(Project.id == callback_query.from_user.id)
    instance = ProjectCreator(project_cursor.creator,
                              project_cursor.theme,
                              project_cursor.description,
                              project_cursor.current_partners,
                              project_cursor.required_partners)

    await bot.send_message(callback_query.from_user.id, instance)
