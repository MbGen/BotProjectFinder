from aiogram import executor

from loader import dp

import filters, handlers, models

if __name__ == '__main__':
    executor.start_polling(dp)