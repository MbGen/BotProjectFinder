from aiogram import executor

from loader import dp

import filters
import handlers
import models


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
