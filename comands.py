from aiogram import Router,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name} я бот.')



