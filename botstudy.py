 import asyncio

import aiogram
from aiogram import Bot, Dispatcher, types

token: str = '7280734429:AAHaUwW9B6aqRdygZak0U14KLl1NX5OG1is'

bot = Bot(token)
dp = Dispatcher()

@dp.message_handler()

async def hello():
    print('Hello, Welcome to SENATOROV Education!')

if__name__ == '__main__'
