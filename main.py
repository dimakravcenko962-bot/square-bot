from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
  await message.answer("Привіт! Я ваш новий бот для Binance Square. Готовий до роботи!")


# Чіткий обробник для слова "пост" (реагує і на "Пост", і на "пост")
@dp.message(F.text.lower() == "пост")
async def handle_post(message: types.Message):
  await message.answer("📝 Готую ідею для поста...")


# Чіткий обробник для слова "аналіз"
@dp.message(F.text.lower().contains("аналіз"))
async def handle_analysis(message: types.Message):
  await message.answer("📊 Роблю аналіз ринку...")


async def main():
  await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == "__main__":
  asyncio.run(main())
