from decouple import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio, logging
from hendler.handlers import router
from hendler.vredprivichki import vred
from hendler.cel import cel
from hendler.start import start
from hendler.start2 import start2
from datetime import datetime, date
import pytz     #   pip install pytz


mos = pytz.timezone('Europe/Moscow')
moscow_time = datetime.now(mos)

day_15 = datetime(moscow_time.year, moscow_time.month, moscow_time.day, 16,0,0).astimezone(mos)
day_0 = datetime(moscow_time.year, moscow_time.month, moscow_time.day, 1,0,0).astimezone(mos)

rout = start if day_0 < moscow_time <  day_15 else start2

bot = Bot(token=config('API_TOKEN'))
dp = Dispatcher()
channel_id = config('CHANNEL_ID')



async def main():
    # await send_message(channel_id, 'Hello')   #dp.start_polling(bot)
    # dp.include_router(cel)
    # dp.include_router(vred)
    # dp.include_router(router)
    dp.include_router(rout)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')