from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback_data import CallbackDataEnum


class Authorization:

    @staticmethod
    def authorize_kb() -> InlineKeyboardMarkup:
        authorize_inline_btn = InlineKeyboardButton("Заполнить информацию о себе",
                                                    callback_data=CallbackDataEnum.AUTHORIZATION.value)
        authorization_inline_kb = InlineKeyboardMarkup().add(authorize_inline_btn)
        return authorization_inline_kb
