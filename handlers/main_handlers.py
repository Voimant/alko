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
    if mess.from_user.id == 34534543:
        await mess.answer('Кирилл гей❤️')
        print(mess.from_user.id)
        print(mess.from_user.full_name)

    else:
        print(mess.from_user.id)
        print(mess.from_user.full_name)

# 751342903 - саша


