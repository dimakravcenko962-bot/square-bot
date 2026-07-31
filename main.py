import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Бот для Binance Square працює! 🚀")

@dp.message()
async def handle_message(message: types.Message):
    if not message.text:
        return
    
    text = message.text.lower()
    
    if "пост" in text:
        await message.answer("📝 Готую ідею для поста...")
    elif "аналіз" in text:
        await message.answer("📊 Роблю аналіз ринку...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
