from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback_data import AuthorizationCallback, ThemeCallback, TypeOfUserCallback, MenuCallback, ProfileCallback


class AuthorizationKB:

    @staticmethod
    def get_authorize_kb() -> InlineKeyboardMarkup:
        authorize_inline_btn = InlineKeyboardButton(text="🧑Заполнить информацию о себе",
                                                    callback_data=AuthorizationCallback.AUTHORIZATION)

        authorization_inline_kb = InlineKeyboardMarkup(row_width=1).add(authorize_inline_btn)
        return authorization_inline_kb

    @staticmethod
    def get_choice_theme_kb() -> InlineKeyboardMarkup:
        theme_inline_btns = (
            InlineKeyboardButton(text="Боты", callback_data=ThemeCallback.BOTS),
            InlineKeyboardButton(text="Веб", callback_data=ThemeCallback.WEB),
        )

        theme_inline_kb = InlineKeyboardMarkup(row_width=1).add(*theme_inline_btns)
        return theme_inline_kb

    @staticmethod
    def get_choice_type_of_user_kb() -> InlineKeyboardMarkup:
        type_of_user_btns = (
            InlineKeyboardButton(text="Искать", callback_data=TypeOfUserCallback.SEARCHER),
            InlineKeyboardButton(text="Создавать", callback_data=TypeOfUserCallback.CREATOR),
        )

        type_of_user_kb = InlineKeyboardMarkup(row_width=1).add(*type_of_user_btns)
        return type_of_user_kb


class MenuKB:
    @staticmethod
    def get_menu_kb() -> InlineKeyboardMarkup:
        main_menu_btns = (
            InlineKeyboardButton(text="📜Список проектов", callback_data=MenuCallback.LIST_OF_PROJECTS),
            InlineKeyboardButton(text="🙋‍♂️Профиль", callback_data=MenuCallback.PROFILE)
        )

        main_menu_kb = InlineKeyboardMarkup().add(*main_menu_btns)
        return main_menu_kb


class ProfileKB:
    @staticmethod
    def get_creator_kb() -> InlineKeyboardMarkup:
        creator_btns = (
            InlineKeyboardButton(text="Мое описание", callback_data=ProfileCallback.ABOUT_ME),
            InlineKeyboardButton(text="Создать проект", callback_data=ProfileCallback.CREATE_PROJ),
            InlineKeyboardButton(text="Меню", callback_data=MenuCallback.MAIN_MENU)
        )

        creator_kb = InlineKeyboardMarkup().add(*creator_btns)
        return creator_kb

    @staticmethod
    def get_searcher_kb() -> InlineKeyboardMarkup:
        searcher_btns = (
            InlineKeyboardButton(text="Мое описание", callback_data=ProfileCallback.ABOUT_ME),
            InlineKeyboardButton(text="Меню", callback_data=MenuCallback.MAIN_MENU)
        )

        searcher_kb = InlineKeyboardMarkup().add(*searcher_btns)
        return searcher_kb
