from aiogram.dispatcher.filters.state import State, StatesGroup


class ProjectAdd(StatesGroup):
    waiting_for_description = State()
    waiting_for_partners_amount = State()
