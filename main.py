import asyncio

from aiogram import Bot, Dispatcher
from app.test import router

async def main():
    bot = Bot(token='7530313667:AAG-kqhEUNv0qi3N5s8ARA8Gn1XpxyVpOwU')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('bot started')
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot deactivated")
