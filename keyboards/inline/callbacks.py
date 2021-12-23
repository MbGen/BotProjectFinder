from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback_data import CallbackData


class AuthorizationKB:

    @staticmethod
    def authorize_kb() -> InlineKeyboardMarkup:
        authorize_inline_btn = InlineKeyboardButton(text="Заполнить информацию о себе",
                                                    callback_data=CallbackData.AUTHORIZATION)
        authorization_inline_kb = InlineKeyboardMarkup(row_width=1).add(authorize_inline_btn)
        return authorization_inline_kb

    @staticmethod
    def choice_theme_kb() -> InlineKeyboardMarkup:
        theme_inline_btns = (
            InlineKeyboardButton(text="Боты", callback_data=CallbackData.BOTS),
            InlineKeyboardButton(text="Веб", callback_data=CallbackData.WEB),
        )
        theme_inline_kb = InlineKeyboardMarkup(row_width=1).add(*theme_inline_btns)
        return theme_inline_kb

    @staticmethod
    def choice_type_of_user() -> InlineKeyboardMarkup:
        type_of_user_btns = (
            InlineKeyboardButton(text="Искать", callback_data=CallbackData.SEARCHER),
            InlineKeyboardButton(text="Создавать", callback_data=CallbackData.CREATOR),
        )

        type_of_user_kb = InlineKeyboardMarkup(row_width=1).add(*type_of_user_btns)
        return type_of_user_kb
