import asyncio
from aiogram import Bot,Dispatcher
import logging
from config import TOKEN_AIOBOT
from comands import router


# Включаем логирование, чтобы не пропустить важные сообщения

# Объект бота
bot = Bot(TOKEN_AIOBOT)
# Диспетчер
dp = Dispatcher()



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    dp.include_router(router)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
