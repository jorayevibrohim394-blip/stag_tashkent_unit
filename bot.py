"""
AvtoGaz Telegram Boti - Asosiy ishga tushiruvchi fayl (main entry point)
"""
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers import router

# Loglarni sozlash
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

async def set_bot_commands(bot: Bot):
    """Telegram ilovasida menyu tugmasidagi buyruqlar ro'yxati"""
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="ai", description="AI Usta bilan suhbat"),
        BotCommand(command="clearchat", description="Suhbat tarixini tozalash"),
        BotCommand(command="kalkulyator", description="Yoqilg'i tejash kalkulyatori"),
        BotCommand(command="metan", description="Metan (CNG) ma'lumotlari"),
        BotCommand(command="propan", description="Propan (LPG) ma'lumotlari"),
        BotCommand(command="taqqoslash", description="Metan vs Propan taqqoslash"),
        BotCommand(command="reduktor", description="Gaz reduktori bo'limi"),
        BotCommand(command="farsunka", description="Gaz farsunkalari bo'limi"),
        BotCommand(command="xavfsizlik", description="Balonlar va xavfsizlik"),
        BotCommand(command="nosozliklar", description="Nosozliklar va yechimlar"),
        BotCommand(command="help", description="Yordam va qo'llanma")
    ]
    await bot.set_my_commands(commands)

async def main():
    if not BOT_TOKEN or "TOKEN" in BOT_TOKEN and len(BOT_TOKEN) < 20:
        logger.error("BOT_TOKEN ko'rsatilmagan yoki noto'g'ri!")
        return

    # Bot va Dispatcher yaratish
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Handler routerini ulash
    dp.include_router(router)

    # Bot buyruqlarini ro'yxatdan o'tkazish
    await set_bot_commands(bot)

    # Bot ma'lumotlarini olish va logda ko'rsatish
    me = await bot.get_me()
    logger.info(f"AvtoGaz Bot muvaffaqiyatli ishga tushdi: @{me.username} (ID: {me.id})")
    print(f"\n==========================================")
    print(f" AvtoGaz Bot ishga tushdi: @{me.username}")
    print(f" Telegramdan @{me.username} ga kiring va /start bosing!")
    print(f"==========================================\n")

    # Eski kutilayotgan xabarlarni tozalash
    await bot.delete_webhook(drop_pending_updates=True)

    # Pollingni boshlash
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi.")
