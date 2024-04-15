import random

from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery
import wikipedia
from dotenv import load_dotenv
from aiogram import Bot
import os


wikipedia.set_lang('ru')
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
router = Router()


@router.message(Command('wiki'))
async def wiki(mess: Message, command: CommandObject):
    result = command.args
    result_list = result.split(' ')
    try:
        out = wikipedia.summary(f"{result_list[0]}", sentences=4)
        print(result)
        await mess.answer(out)
    except Exception as e:
        print(e)
        await mess.answer("Я не в курсе :( может в следующий раз")




@router.message()
async def my_id(mess: Message):
        x = random.randint(1, 10)
        if x == 1:
            await mess.answer('Хорошего настроения и приятного дня :)')
        elif x == 2:
            pass
        elif x == 3:
            await mess.answer('Алко пати! вы лучшие, рада быть в вашей команде!')
        elif x == 4:
            pass


