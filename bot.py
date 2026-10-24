"""
AvtoGaz Telegram Boti - Asosiy ishga tushiruvchi fayl (main entry point)
Render.com Web Service va Background Worker bilan to'liq moslashgan.
Doimiy 24/7 ishlash uchun avtomatik Keep-Alive mexanizmiga ega.
"""
import asyncio
import logging
import os
import sys

import aiohttp
from aiohttp import web
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

async def health_check_handler(request):
    """Render.com uchun HTTP health-check tekshiruvi"""
    return web.Response(text="AvtoGaz Bot is running successfully 24/7! 🚗💨", content_type="text/plain")

async def start_dummy_web_server():
    """
    Render.com Web Service rejimida portni tinglaydi.
    PORT muhit o'zgaruvchisi (odatda 10000) orqali darhol 0.0.0.0 da HTTP server ochadi.
    """
    port = int(os.getenv("PORT", "10000"))
    try:
        app = web.Application()
        app.router.add_get("/", health_check_handler)
        app.router.add_get("/health", health_check_handler)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()
        logger.info(f"Render uchun HTTP server 0.0.0.0:{port}-portda muvaffaqiyatli ishga tushdi.")
        print(f"==> Port {port} ochiq va tinglanmoqda (Render Web Service live).", flush=True)
    except Exception as e:
        logger.warning(f"HTTP serverni ishga tushirishda xatolik: {e}")

async def render_keep_alive():
    """
    Render bepul tarifida 15 daqiqada uxlab qolmasligi uchun
    har 10 daqiqada o'ziga o'zi HTTP so'rov yuborib turadi (24/7 hushyor saqlash).
    """
    url = os.getenv("RENDER_EXTERNAL_URL")
    if not url:
        return

    logger.info(f"Render Keep-Alive faollashtirildi: {url}")
    await asyncio.sleep(60)  # Dastlab 1 daqiqa kutish

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                ping_url = f"{url.rstrip('/')}/health"
                async with session.get(ping_url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                    logger.info(f"Render Keep-Alive ping muvaffaqiyatli: {resp.status}")
            except Exception as e:
                logger.warning(f"Render Keep-Alive ping xatosi: {e}")
            await asyncio.sleep(600)  # Har 10 daqiqada bir marta

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
    if not BOT_TOKEN or ("TOKEN" in BOT_TOKEN and len(BOT_TOKEN) < 20):
        logger.error("BOT_TOKEN ko'rsatilmagan yoki noto'g'ri!")
        return

    # 1. Render Web Service uchun portni ochish
    await start_dummy_web_server()

    # 2. Render uxlamasligi uchun fonda Keep-Alive vazifasini ishga tushirish
    asyncio.create_task(render_keep_alive())

    # 3. Bot va Dispatcher yaratish
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
    print(f"==========================================\n", flush=True)

    # Kutilayotgan xabarlarni o'chirmasdan qabul qilib olish
    await bot.delete_webhook(drop_pending_updates=False)

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
