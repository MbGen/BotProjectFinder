from loader import dp, bot
from aiogram import types, filters
import aiogram.utils.markdown as fmt
from keyboards import inline
from keyboards.inline.callback_data import ProfileCallback
from models.project import Project


creation_theme_kb = inline.callbacks.ProjectCreationKB.get_themes_kb()


@dp.callback_query_handler(text_contains=ProfileCallback.CREATE_PROJ)
async def start_creation(callback_query: types.CallbackQuery) -> None:
    Project.get_or_create(id=callback_query.from_user.id, creator=callback_query.from_user.username)
    await bot.send_message(callback_query.from_user.id,
                           "<strong>Выберите тему</strong>",
                           reply_markup=creation_theme_kb
                           )
