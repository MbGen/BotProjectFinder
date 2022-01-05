from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class MenuKB:
    @staticmethod
    def get_menu_kb() -> ReplyKeyboardMarkup:
        menu_btn = KeyboardButton(text="/menu")
        menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_btn)
        return menu_kb
