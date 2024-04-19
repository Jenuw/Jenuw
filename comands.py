import random

from aiogram import Router,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
import inkinekeyboard as ik
from random import randint

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!",reply_markup=ik.keyboard)

@router.message(Command('help'))
async def cmm_help(message: Message):
    await message.answer('в данный момент этот бот ничего не умеет')

@router.message(F.text=='Случайное число')
async def randomize (message: Message):
    await message.answer(str(random.randint(1,11)))


