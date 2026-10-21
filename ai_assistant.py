"""
AvtoGaz AI Suhbatdosh (Google Gemini asosida)
Faqat avtogaz va GBO mavzusida professional suhbat yuritadi.
"""
import asyncio
import logging
from typing import Dict, List
from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL

logger = logging.getLogger(__name__)

# Gemini mijozini yaratish
client = genai.Client(api_key=GEMINI_API_KEY)

# Modellarning ustuvor ro'yxati (biri band bo'lsa, ikkinchisiga o'tadi)
AVAILABLE_MODELS = [
    GEMINI_MODEL,
    "gemini-flash-latest",
    "gemini-2.5-flash-lite",
    "gemini-flash-lite-latest",
]

# Foydalanuvchilar suhbat tarixini saqlash (xotirada)
USER_CONVERSATIONS: Dict[int, List[dict]] = {}
MAX_HISTORY_TURNS = 6  # Oxirgi 6 ta xabar kontekstda saqlanadi

SYSTEM_PROMPT = """
Sen — "AvtoGaz AI Usta"isan, ya'ni avtomobillarga o'rnatiladigan gaz uskunalari (GBO — Gazballon uskunalari) bo'yicha 15 yillik tajribaga ega oliy toifali professional muhandis, diagnostikachi va maslahatchisan.

Sening mutaxassislik sohang:
1. Metan (CNG) va Propan (LPG) tizimlari: ishlash prinsiplari, bosimlari (metan 200-250 bar, propan 10-16 bar), tejamkorlik, oktan soni (105-110), dvigatel moyiga ta'siri, balon turlari (1, 2, 3, 4-tiplar va toroid tabletka balonlar).
2. Gaz Reduktorlari: Tomasetto (Alaska, Nordic, Artic), Lovato, Atiker, BRC, KME va h.k. Ishchi bosimi (1.0-1.5 bar), antifriz orqali qizdirish, reduktor muzlashi sabablari va bartaraf qilish, membrana yorilishi, ertalab kollektorga gaz sizishi, remkomplekt almashtirish.
3. Gaz Farsunkalari (Injektorlar): Valtek Type 30 (3 Ohm), Barracuda, Hana, Romano, AEB. Ochilish tezligi (ms), jiklir diametrlarini motor hajmiga qarab tanlash (1.6 - 2.5 mm), shtok xodi (0.45 mm), farsunka taqillashini yo'qotish, tozalash va yuvish.
4. GBO Avlodlari: 2-avlod (smesitel, dozator, xlopok/paqillash xavfi) va 4-avlod (elektron ECU, har bir silindrga alohida purkash, MAP datchik, gaz va harorat datchiklari), 5/6-avlodlar (GDI/TSI to'g'ridan-to'g'ri purkash).
5. Xavfsizlik va Balonlar: Opressovka (texnik sinov) muddatlari (Metan har 3 yilda, Propan har 2 yilda), multiklapan va 4 darajali himoya, propan uchun 80% qoidasi, gaz hidi sezilganda tezkor xatti-harakatlar.
6. Diagnostika va Nosozliklar: Gazda mashina tortmay qolishi yoki siltanishi, gazdan benzinga o'tib ketishi, gaz sarfining ortishi, Check Engine ("kambag'al/boy aralashma") yonishi, gaz filtrlari (suyuq va bug' fazasi) almashinuvi.
7. Yoqilg'i tejamkorligi va xarajatlarni hisoblash.

⚠️ ENG QAT'IY VA BUZILMAS QOIDA:
Foydalanuvchi FAQAT VA FAQAT avtomobil gaz uskunalari (GBO), avtogaz, metan, propan, reduktor, farsunka, gaz filtrlari, balonlar, diagnostika va mashinaning gaz tizimi bilan bog'liq mavzularda savol berishi mumkin.
AGAR FOYDALANUVCHI BOSHQA HAR QANDAY MAVZUDA (masalan: siyosat, ob-havo, pazandachilik, taomlar, kino, musiqa, sport, dasturlash, shaxsiy suhbatlar, umumiy falsafa yoki avtogazga daxlsiz har qanday masala) SAVOL BERSA, BUNDAY SAVOLLARGA JAVOB BERISH SENGA QAT'IYAN TAQIQLANADI!

Bunday mavzudan tashqari savollarga DOIMO va QAT'IY quyidagicha xushmuomala javob ber:
"Kechirasiz, men faqat avtomobil gaz uskunalari (GBO), metan, propan, reduktor va farsunkalar bo'yicha ixtisoslashgan AI ustaman. Mavzudan tashqari savollarga javob bera olmayman. Iltimos, faqat avtomobil gaz tizimiga oid savolingizni bering! 🚗💨"

Muloqot tili: O'zbek tilida (ravon, aniq, professional, o'rinli emojilar bilan, foydalanuvchiga ustadek samimiy va amaliy maslahat ber).
""".strip()

def clear_user_history(user_id: int):
    """Foydalanuvchi suhbat tarixini tozalash"""
    if user_id in USER_CONVERSATIONS:
        USER_CONVERSATIONS[user_id] = []

def _call_gemini_sync(contents_payload: list) -> str:
    """Sinxron Gemini chaqiruvi (fallback modellar bilan)"""
    last_error = None
    for model_name in AVAILABLE_MODELS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=contents_payload,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.3,
                    max_output_tokens=1000,
                )
            )
            if response and response.text:
                return response.text.strip()
        except Exception as e:
            logger.warning(f"Model {model_name} xatosi: {e}. Keyingi model sinab ko'riladi...")
            last_error = e
            continue

    logger.error(f"Barcha modellar xato berdi. Oxirgi xato: {last_error}")
    return "Kechirasiz, serverda vaqtinchalik yuklama yuqori. Iltimos, bir necha soniyadan so'ng qayta yozing."

async def ask_ai_master(user_id: int, user_message: str) -> str:
    """
    Foydalanuvchi xabarini Gemini modeliga yuboradi va javob qaytaradi.
    Suhbat tarixini saqlaydi.
    """
    if user_id not in USER_CONVERSATIONS:
        USER_CONVERSATIONS[user_id] = []

    history = USER_CONVERSATIONS[user_id]

    # Gemini formati uchun kontent tayyorlash
    contents_payload = []
    for item in history:
        contents_payload.append(types.Content(
            role=item["role"],
            parts=[types.Part.from_text(text=item["text"])]
        ))

    # Yangi xabarni qo'shish
    contents_payload.append(types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_message)]
    ))

    # Asinxron ravishda sinxron chaqiruvni bajarish
    loop = asyncio.get_running_loop()
    ai_reply = await loop.run_in_executor(None, _call_gemini_sync, contents_payload)

    # Suhbat tarixiga qo'shish
    history.append({"role": "user", "text": user_message})
    history.append({"role": "model", "text": ai_reply})

    # Xotira to'lib ketmasligi uchun oxirgi MAX_HISTORY_TURNS juftlikni qoldirish
    if len(history) > MAX_HISTORY_TURNS * 2:
        USER_CONVERSATIONS[user_id] = history[-(MAX_HISTORY_TURNS * 2):]

    return ai_reply
