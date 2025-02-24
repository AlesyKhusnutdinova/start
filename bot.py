import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config

from tg_API.handlers import questions, word_processing

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
bot = Bot(token=config.bot_token.get_secret_value())


async def main():
    dp.include_routers(questions.router, word_processing.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
