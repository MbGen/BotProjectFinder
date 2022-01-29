from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.user.add_project import ProjectAdd
from models.project import Project


@dp.message_handler(state=ProjectAdd.waiting_for_partners_amount)
async def add_partners(msg: types.Message, state: FSMContext) -> None:
    try:
        amount = int(msg.text)
        project_cursor = Project.get(Project.id == msg.from_user.id)
        project_cursor.required_partners = amount
        project_cursor.save()
        await state.finish()
        await msg.answer("Проект успешно создан, можете посмотреть в своем профиле")

    except ValueError:
        await msg.answer("Введите целое число")
        await state.set_state(ProjectAdd.waiting_for_partners_amount)
