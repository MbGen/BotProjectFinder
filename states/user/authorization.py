from aiogram.dispatcher.filters.state import State, StatesGroup

#TODO: разбить по файлам
class Authorization(StatesGroup):
    waiting_for_nick = State()
    waiting_for_age = State()
    waiting_for_theme = State()
    waiting_for_skills = State()
    waiting_for_about = State()
    waiting_for_type_of_user = State()
