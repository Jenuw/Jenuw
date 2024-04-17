from aiogram import Router,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!")

@router.message(Command('help'))
async def cmm_help(message: Message):
    await message.answer('в данный момент этот бот ничего не умеет')


