from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.add_project import ProjectAdd
from models.project import Project


@dp.message_handler(state=ProjectAdd.waiting_for_description)
async def add_description(msg: types.Message, state: FSMContext) -> None:
    project_cursor = Project.get(Project.id == msg.from_user.id)
    project_cursor.description = msg.text
    project_cursor.save()
    await ProjectAdd.next()
    await msg.answer("А теперь напишите требуемое кол-во участников")
