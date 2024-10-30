import asyncio
import os
import random
import time
from asyncio import sleep


from aiogram.types import FSInputFile
from dotenv import load_dotenv
from aiogram import Bot

from wiki import update_token, neiro

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
PIC_PATH = os.getenv('PIC_PACH')


async def get_mem_day():
    update_token()
    response = neiro('оригинально пожелай друзьям доброго утра и в конце напиши "ОЖИДАЕМ БУСЮ ДНЯ!"')
    await bot.send_message(-1001818033439, f'{response}')

