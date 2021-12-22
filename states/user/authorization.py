from aiogram.dispatcher.filters.state import State, StatesGroup


class Authorization(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_age = State()
    waiting_for_theme = State()
    waiting_for_skills = State()
    waiting_for_about = State()
    waiting_for_type_of_user = State()
