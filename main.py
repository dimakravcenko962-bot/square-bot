import os, asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(m: types.Message):
    await m.answer("Привіт! Бот для Binance Square працює! 🚀")

@dp.message(F.text.func(lambda t: "пост" in t.lower()))
async def post(m: types.Message):
    await m.answer("📝 Готую ідею для поста...")

@dp.message(F.text.func(lambda t: "аналіз" in t.lower()))
async def analysis(m: types.Message):
    await m.answer("📊 Роблю аналіз ринку...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
