# 🚗 AvtoGaz Telegram Boti

Avtomobillarga gaz o'rnatish uskunalari (**GBO**) bo'yicha to'liq va professional ma'lumot beruvchi Telegram boti.

## 📌 Botning imkoniyatlari
- ⛽ **Metan (CNG):** Ishlash prinsipi, bosimi (200-250 bar), afzallik va kamchiliklari, 4 xil balon tiplari.
- 🛢 **Propan (LPG):** Suyuq neft gazi, bosimi (10-16 bar), afzalliklari, zapaska o'rniga tushadigan Toroid ("Tabletka") balonlar.
- ⚖️ **Metan vs Propan taqqoslash:** Qaysi biri qanday haydovchilarga mos kelishi bo'yicha batafsil taqqoslash jadvali.
- ⚙️ **Gaz Reduktori:** Tomasetto, Lovato, Atiker brendlari, nosozliklar (muzlab qolishi, gaz hidi, ertalab zo'rg'a o't olishi), remkomplekt almashtirish va sozlash.
- 🔌 **Gaz Farsunkalari:** Valtek vs Barracuda solishtiruvi, jiklir teshiklarini to'g'ri kalibrlash, farsunka taqillashini yo'qotish va tozalash.
- 🚗 **GBO Avlodlari:** 2-avlod va 4-avlod taqqoslashi, afzallik va kamchiliklari.
- 🧯 **Gaz Balonlari va Xavfsizlik:** Opressovka (texnik sinov) muddatlari, multiklapan himoyalari, yozgi va qishki zapravka qoidalari.
- 🛠 **Nosozliklar va Yechimlar:** Gazda yuradigan avtomobillarda uchraydigan 8 ta asosiy muammo va ularni bartaraf qilish.
- 💰 **Yoqilg'i tejash kalkulyatori:** 100 km va 10 000 km masofada Benzin, Metan va Propan xarajatlari hamda tejaladigan sof foydani aniq hisoblash.

---

## 🚀 Botni ishga tushirish

### 1-usul: Tayyor `.bat` fayl orqali (Eng oson)
Fayllar turgan papkadagi `run_bot.bat` fayliga sichqoncha bilan ikki marta bosing.

### 2-usul: Terminal (PowerShell / CMD) orqali:
```bash
python bot.py
```

---

## 📁 Loyiha tarkibi:
- `bot.py` — Botni ishga tushiruvchi asosiy fayl (Dispatcher, Polling)
- `handlers.py` — Foydalanuvchi buyruqlari, tugmalar va kalkulyator mantiqi
- `content.py` — Barcha avtogaz ma'lumotlari, matnlar va jadvallar
- `keyboards.py` — Asosiy menyu (Reply) va qulay Inline tugmalar
- `calculator.py` — Yoqilg'i tejamkorligini hisoblovchi algoritm
- `config.py` — Bot tokeni va o'rtacha yoqilg'i narxlari
- `run_bot.bat` — Windows uchun bitta bosishda ishga tushiruvchi fayl
- `requirements.txt` — Kerakli kutubxonalar (`aiogram`)
