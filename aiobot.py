import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN_AIOBOT

# Включаем логирование, чтобы не пропустить важные сообщения

# Объект бота
bot = Bot(TOKEN_AIOBOT)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
