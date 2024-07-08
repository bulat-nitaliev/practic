from decouple import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio, logging
from hendler.handlers import router
from hendler.vredprivichki import vred
from hendler.cel import cel

bot = Bot(token=config('API_TOKEN'))
dp = Dispatcher()
channel_id = config('CHANNEL_ID')



async def main():
    # await send_message(channel_id, 'Hello')   #dp.start_polling(bot)
    dp.include_router(cel)
    dp.include_router(vred)
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')