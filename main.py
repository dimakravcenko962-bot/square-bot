import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8655828629:AAHGBz0sUYsio4PtV-9Rz8mgCQLVV4u-lHs"

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Я твій новий помічник для Binance Square. Готовий до роботи! 🚀")

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
