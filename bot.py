import asyncio
import os
import logging

import aiocron
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

import handlers.main_handlers
from handlers.func_mem import get_mem_day


async def main():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(handlers.main_handlers.router,)
    aiocron.crontab('05 30 * * *', func=get_mem_day, start=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
