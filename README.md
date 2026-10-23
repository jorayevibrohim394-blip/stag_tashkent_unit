# 🚗 AvtoGaz Telegram Boti (GBO & AI Usta)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Aiogram 3.x](https://img.shields.io/badge/Aiogram-3.x-2ca5e0.svg)](https://docs.aiogram.dev/)
[![Gemini AI](https://img.shields.io/badge/Google%20Gemini-3.8%20Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Avtomobillarga gaz uskunalari (**GBO**) o'rnatish, ta'mirlash, sozlash hamda yoqilg'i tejash bo'yicha to'liq ma'lumot beruvchi va **Google Gemini AI** asosidagi professional "AI Usta" suhbatdoshiga ega Telegram boti.

Telegramda bot manzili: **[@stag_tashkent_unitbot](https://t.me/stag_tashkent_unitbot)**

---

## 🌟 Botning asosiy imkoniyatlari

### 1. 🤖 "AvtoGaz AI Usta" sun'iy intellekt suhbatdoshi
- Google Gemini (gemini-3.8-flash) asosidagi professional mutaxassis.
- Gaz bo'yicha har qanday savolga (nosozliklar, mos keluvchi uskunalar, reduktor/farsunka sozlamalari) aniq va amaliy tavsiyalar beradi.
- **Qat'iy mavzu filtri:** Faqat avtomobil gaz uskunalari bo'yicha javob beradi, mavzudan tashqari begona savollarni muloyimlik bilan rad etadi.
- Kontekst xotirasi va suhbat tarixini tozalash imkoniyati (`/clearchat`).

### 2. ⛽ Metan (CNG) bo'limi
- Siqilgan tabiiy gaz (200-250 bar) xususiyatlari, afzallik va kamchiliklari.
- Metan balonlarining 4 xil tipi (1-tip to'liq po'lat, 2-tip kompozit, 3-tip alyuminiy-uglerod, 4-tip polimer kompozit).

### 3. 🛢 Propan (LPG) bo'limi
- Suyuq neft gazi (10-16 bar), xavfsizlik darajasi, yurish masofasi (400-600 km).
- Zapaska o'rniga tushadigan Toroid ("Tabletka") balonlar haqida batafsil ma'lumot.

### 4. ⚖️ Metan vs Propan taqqoslash
- Bosim, og'irlik, masofa, quvvat yo'qotishi, xavfsizlik va narx bo'yicha taqqoslash jadvali.
- Haydovchining yurish rejimiga qarab qaysi biri mos kelishini aniqlash.

### 5. ⚙️ Gaz Reduktori (GBO yuragi)
- Tomasetto (Alaska, Nordic, Artic), Lovato, Atiker, BRC brendlari.
- Reduktor muzlashi sabablari va tezkor bartaraf qilish choralari.
- Membrana yorilishi, ertalab kollektorga gaz to'planishi, remkomplekt almashtirish vaqtlari.

### 6. 🔌 Gaz Farsunkalari (Injektorlar)
- Valtek (3 Ohm) va tezkor Barracuda/Hana farqlari.
- Motor hajmiga qarab jiklir teshigi diametrlarini (1.6mm — 2.5mm) to'g'ri kalibrlash.
- Farsunka "chiq-chiq" taqillashini yo'qotish va stendda tozalash.

### 7. 🚗 GBO Avlodlari
- 2-avlod (smesitel, xlopok/paqillash xavfi) va 4-avlod (elektron ECU, taqsimlangan purkash) solishtiruvi.
- 5 va 6-avlod to'g'ridan-to'g'ri purkash (GDI, TSI) haqida.

### 8. 🧯 Gaz Balonlari va Xavfsizlik
- Opressovka (texnik sinov) muddatlari: Metan har 3 yilda, Propan har 2 yilda.
- Multiklapan va himoya darajalari, 80% qoidasi, gaz hidi sezilganda xatti-harakatlar.

### 9. 🛠 Keng tarqalgan nosozliklar va yechimlar
- Mashina gazda tortmasligi yoki siltanishi.
- Gazdan o'z-o'zidan benzinga o'tib ketishi.
- Gaz hidi salonga kirishi.
- Check Engine chirog'i yonishi ("kambag'al aralashma").

### 10. 💰 Yoqilg'i tejash kalkulyatori
- 100 km va 10 000 km masofada Benzin (AI-92), Metan va Propan xarajatlarini hamda tejaladigan sof foydani aniq hisoblash.

---

## 📁 Loyiha tarkibi

```text
├── bot.py                # Asosiy ishga tushiruvchi fayl (Dispatcher, Polling)
├── ai_assistant.py       # Gemini AI suhbatdosh mantiqi va prompt filtri
├── handlers.py           # Buyruqlar, tugmalar va foydalanuvchi xabarlarini qayta ishlash
├── content.py            # Avtogaz bo'yicha to'liq ma'lumotlar bazasi
├── keyboards.py          # Reply va Inline klaviaturalar
├── calculator.py         # Yoqilg'i sarfi va tejamkorlik algoritmi
├── config.py             # Konfiguratsiya va .env faylini yuklovchi
├── .env.example          # API kalitlar uchun namuna
├── .gitignore            # Git kuzatuvidan chiqarilgan fayllar
├── requirements.txt      # Kutubxonalar ro'yxati (aiogram, google-genai)
├── run_bot.bat           # Windows uchun bir bosishda botni ishga tushirish
└── push_to_github.bat    # Bir bosishda yangilanishlarni GitHub'ga yuklash
```

---

## 🚀 O'rnatish va ishga tushirish

### 1. Repozitoriyadan nusxa olish:
```bash
git clone https://github.com/jorayevibrohim394-blip/stag_tashkent_unit.git
cd stag_tashkent_unit
```

### 2. Kerakli kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

### 3. Maxfiy kalitlarni sozlash (`.env`):
`.env.example` faylidan `.env` nusxasini yarating va kalitlarni kiriting:
```ini
BOT_TOKEN=Sizning_Telegram_Bot_Tokeningiz
GEMINI_API_KEY=Sizning_Gemini_API_Kalitingiz
```

### 4. Botni ishga tushirish:
**Windows foydalanuvchilari uchun:**
Papkadagi `run_bot.bat` faylini ikki marta bosing.

**Terminal orqali:**
```bash
python bot.py
```

---

## 📞 Muallif va Bog'lanish
- GitHub: [@jorayevibrohim394-blip](https://github.com/jorayevibrohim394-blip)
- Telegram Bot: [@stag_tashkent_unitbot](https://t.me/stag_tashkent_unitbot)
