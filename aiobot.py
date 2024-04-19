import asyncio
from aiogram import Bot, Dispatcher, types
import logging
from comands import router
from dotenv import load_dotenv
import os


# Включаем логирование, чтобы не пропустить важные сообщения
load_dotenv()
# Объект бота
bot = Bot(os.getenv('TOKEN'))
# Диспетчер
dp = Dispatcher()






async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())