from loader import dp, bot
from aiogram import types, filters
from keyboards import inline
import aiogram.utils.markdown as fmt


creator_project_callback = inline.callback_data.ProfileCallback.MY_PROJ_CREATOR
searcher_project_callback = inline.callback_data.ProfileCallback.MY_PROJ_SEARCHER


@dp.callback_query_handler(text_contains=creator_project_callback)
async def get_creator_project(callback_query: types.CallbackQuery) -> None:
    await bot.send_message(callback_query.from_user.id, fmt.text(fmt.bold("Ваш проект")))
