from decouple import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio, logging

bot = Bot(token=config('API_TOKEN'))
dp = Dispatcher()
channel_id = config('CHANNEL_ID')

async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


@dp.message(CommandStart)
async def start(message:types.Message):
    print(message.from_user)
    await message.answer('As salamu aleykum')

async def main():
    # await send_message(channel_id, 'Hello')   #dp.start_polling(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')