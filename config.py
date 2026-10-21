"""
AvtoGaz Bot sozlamalari va konfiguratsiyasi
"""
import os
from pathlib import Path

# .env faylidan o'zgaruvchilarni yuklash
env_path = Path(__file__).resolve().parent / ".env"
if env_path.exists():
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key and key not in os.environ:
                        os.environ[key] = val
    except Exception:
        pass

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Google Gemini AI API kaliti
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-3.8-flash"

# Yoqilg'i narxlari (so'mda - kalkulyator uchun o'rtacha ko'rsatkichlar)
PRICE_BENZIN_AI92 = 11000   # 1 litr benzin
PRICE_METAN = 3900          # 1 kub metr metan gaz
PRICE_PROPAN = 5800         # 1 litr propan gaz
