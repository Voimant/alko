import asyncio
import os
import random
import time
from asyncio import sleep

import wikipedia
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from aiogram import Bot

wikipedia.set_lang('ru')
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
PIC_PATH = os.getenv('PIC_PACH')


async def get_mem_day():
    list_mems = os.listdir(f'/root{PIC_PATH}')
    x = random.randint(0, len(list_mems))
    mem_day = list_mems[x]
    file = FSInputFile(f'/root{PIC_PATH}/{str(mem_day)}')
    await bot.send_photo(chat_id=-1001818033439, photo=file, caption=f'Всем привет! Мем дня!')
    await bot.send_message(-1001818033439, '!')

