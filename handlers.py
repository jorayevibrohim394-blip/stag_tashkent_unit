"""
AvtoGaz Telegram boti uchun barcha hodisalar va xabarlarni qayta ishlovchi (handlers)
"""
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ChatAction
from aiogram.exceptions import TelegramBadRequest

from config import PRICE_BENZIN_AI92, PRICE_METAN, PRICE_PROPAN
from content import (
    WELCOME_TEXT,
    AI_INTRO_TEXT,
    HELP_TEXT,
    METAN_INFO,
    PROPAN_INFO,
    TAQQOSLASH_TEXT,
    REDUKTOR_INFO,
    FARSUNKA_INFO,
    GBO_AVLODLARI,
    XAVFSIZLIK_BALONLAR,
    NOSOZLIKLAR_YECHIMLAR,
    TAVSIYALAR_VA_QOIDALAR,
    KALKULYATOR_EXPLAIN
)
from keyboards import (
    get_main_keyboard,
    get_ai_chat_inline,
    get_metan_inline,
    get_propan_inline,
    get_reduktor_inline,
    get_farsunka_inline,
    get_calc_keyboard,
    get_back_inline
)
from calculator import calculate_fuel_economy
from ai_assistant import ask_ai_master, clear_user_history

router = Router()
logger = logging.getLogger(__name__)

class CalcState(StatesGroup):
    waiting_for_consumption = State()

# ----------------- ASOSIY BUYRUQLAR -----------------

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """/start buyrug'i: samimiy salomlashish va bosh menyu chiqarish"""
    await state.clear()
    user_name = message.from_user.first_name or "Haydovchi"
    text = WELCOME_TEXT.format(name=user_name)
    await message.answer(text, reply_markup=get_main_keyboard(), parse_mode="HTML")

@router.message(Command("help"))
async def cmd_help(message: Message):
    """/help buyrug'i: qo'llanma"""
    await message.answer(HELP_TEXT, reply_markup=get_main_keyboard(), parse_mode="HTML")

@router.message(Command("ai"))
@router.message(Command("chat"))
async def cmd_ai_chat(message: Message, state: FSMContext):
    """/ai yoki /chat: Sun'iy intellekt usta bilan suhbat xonasi"""
    await state.clear()
    await message.answer(AI_INTRO_TEXT, reply_markup=get_ai_chat_inline(), parse_mode="HTML")

@router.message(Command("clearchat"))
@router.message(Command("tozalash"))
async def cmd_clear_chat(message: Message):
    """Suhbat tarixini tozalash"""
    clear_user_history(message.from_user.id)
    await message.answer("🧹 <b>AI Usta bilan suhbat tarixi tozalandi!</b> Yangi mavzuda savol berishingiz mumkin.", parse_mode="HTML")

@router.message(Command("metan"))
async def cmd_metan(message: Message):
    await message.answer(METAN_INFO, reply_markup=get_metan_inline(), parse_mode="HTML")

@router.message(Command("propan"))
async def cmd_propan(message: Message):
    await message.answer(PROPAN_INFO, reply_markup=get_propan_inline(), parse_mode="HTML")

@router.message(Command("reduktor"))
async def cmd_reduktor(message: Message):
    await message.answer(REDUKTOR_INFO, reply_markup=get_reduktor_inline(), parse_mode="HTML")

@router.message(Command("farsunka"))
async def cmd_farsunka(message: Message):
    await message.answer(FARSUNKA_INFO, reply_markup=get_farsunka_inline(), parse_mode="HTML")

@router.message(Command("taqqoslash"))
async def cmd_taqqoslash(message: Message):
    await message.answer(TAQQOSLASH_TEXT, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(Command("xavfsizlik"))
async def cmd_xavfsizlik(message: Message):
    await message.answer(XAVFSIZLIK_BALONLAR, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(Command("nosozliklar"))
async def cmd_nosozliklar(message: Message):
    await message.answer(NOSOZLIKLAR_YECHIMLAR, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(Command("kalkulyator"))
async def cmd_kalkulyator(message: Message, state: FSMContext):
    await show_calculator(message, state)

# ----------------- REPLY BUTTON MATNLARI -----------------

@router.message(F.text == "💬 AI Usta bilan suhbat")
async def msg_ai_chat(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(AI_INTRO_TEXT, reply_markup=get_ai_chat_inline(), parse_mode="HTML")

@router.message(F.text == "⛽ Metan (CNG)")
async def msg_metan(message: Message):
    await message.answer(METAN_INFO, reply_markup=get_metan_inline(), parse_mode="HTML")

@router.message(F.text == "🛢 Propan (LPG)")
async def msg_propan(message: Message):
    await message.answer(PROPAN_INFO, reply_markup=get_propan_inline(), parse_mode="HTML")

@router.message(F.text == "⚖️ Metan vs Propan")
async def msg_taqqoslash(message: Message):
    await message.answer(TAQQOSLASH_TEXT, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(F.text == "⚙️ Gaz Reduktori")
async def msg_reduktor(message: Message):
    await message.answer(REDUKTOR_INFO, reply_markup=get_reduktor_inline(), parse_mode="HTML")

@router.message(F.text == "🔌 Gaz Farsunkalari")
async def msg_farsunka(message: Message):
    await message.answer(FARSUNKA_INFO, reply_markup=get_farsunka_inline(), parse_mode="HTML")

@router.message(F.text == "🚗 GBO Avlodlari (2 va 4)")
async def msg_avlodlar(message: Message):
    await message.answer(GBO_AVLODLARI, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(F.text == "🧯 Balonlar va Xavfsizlik")
async def msg_xavfsizlik(message: Message):
    await message.answer(XAVFSIZLIK_BALONLAR, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(F.text == "🛠 Nosozliklar va Yechimlar")
async def msg_nosozliklar(message: Message):
    await message.answer(NOSOZLIKLAR_YECHIMLAR, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(F.text == "📞 Oltin Qoidalar")
async def msg_tavsiyalar(message: Message):
    await message.answer(TAVSIYALAR_VA_QOIDALAR, reply_markup=get_back_inline(), parse_mode="HTML")

@router.message(F.text == "💰 Tejash Kalkulyatori")
async def msg_kalkulyator(message: Message, state: FSMContext):
    await show_calculator(message, state)

# ----------------- KALKULYATOR FUNKSIYASI -----------------

async def show_calculator(message_or_query, state: FSMContext):
    """Kalkulyator oynasini chiqarish"""
    await state.set_state(CalcState.waiting_for_consumption)
    text = KALKULYATOR_EXPLAIN.format(
        benzin_price=PRICE_BENZIN_AI92,
        metan_price=PRICE_METAN,
        propan_price=PRICE_PROPAN
    )
    if isinstance(message_or_query, CallbackQuery):
        await message_or_query.message.edit_text(text, reply_markup=get_calc_keyboard(), parse_mode="HTML")
        await message_or_query.answer()
    else:
        await message_or_query.answer(text, reply_markup=get_calc_keyboard(), parse_mode="HTML")

@router.callback_query(F.data.startswith("calc_val_"))
async def process_calc_choice(call: CallbackQuery, state: FSMContext):
    val_str = call.data.replace("calc_val_", "")
    try:
        val = float(val_str)
        result_text = calculate_fuel_economy(val)
        await call.message.edit_text(result_text, reply_markup=get_calc_keyboard(), parse_mode="HTML")
    except Exception as e:
        logger.error(f"Kalkulyator xatosi: {e}")
        await call.answer("Hisoblashda xatolik yuz berdi.", show_alert=True)
    await call.answer()

@router.callback_query(F.data == "calc_custom")
async def process_calc_custom(call: CallbackQuery, state: FSMContext):
    await state.set_state(CalcState.waiting_for_consumption)
    await call.message.answer(
        "✍️ Avtomobilingizning 100 km uchun benzin sarfini yozing (masalan: <b>8.5</b> yoki <b>11</b>):",
        parse_mode="HTML"
    )
    await call.answer()

@router.message(CalcState.waiting_for_consumption)
async def process_custom_consumption_input(message: Message, state: FSMContext):
    """Foydalanuvchi o'z mashinasi sarfini raqam bilan yozganda"""
    text = message.text.strip().replace(",", ".")
    try:
        val = float(text)
        if val <= 0 or val > 50:
            await message.answer("⚠️ Iltimos, haqiqiy sarf miqdorini kiriting (masalan 4 dan 30 gacha).")
            return
        result_text = calculate_fuel_economy(val)
        await message.answer(result_text, reply_markup=get_calc_keyboard(), parse_mode="HTML")
        await state.clear()
    except ValueError:
        # Agar raqam bo'lmasa, demak savol so'rayapti - AI ga yo'naltiramiz
        await state.clear()
        await handle_ai_user_question(message)

# ----------------- AI BILAN SUHBAT CALLBACKLARI -----------------

@router.callback_query(F.data == "clear_ai_history")
async def cb_clear_ai_history(call: CallbackQuery):
    clear_user_history(call.from_user.id)
    await call.message.answer("🧹 <b>Suhbat tarixi tozalandi!</b> Yangi mavzuda savol berishingiz mumkin.", parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "ask_ai_direct")
async def cb_ask_ai_direct(call: CallbackQuery):
    await call.message.answer("✍️ Gaz uskunasi bo'yicha savolingizni yozib yuboring, men darhol javob beraman:", parse_mode="HTML")
    await call.answer()

# ----------------- BOSHQA INLINE CALLBACKLAR -----------------

@router.callback_query(F.data == "compare_gas")
async def cb_compare(call: CallbackQuery):
    await call.message.answer(TAQQOSLASH_TEXT, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "calc_quick")
async def cb_calc_quick(call: CallbackQuery, state: FSMContext):
    await show_calculator(call, state)

@router.callback_query(F.data == "metan_cylinders")
async def cb_metan_cylinders(call: CallbackQuery):
    text = """
🧯 <b>METAN BALONLARINING 4 XIL TIPI:</b>

1️⃣ <b>1-Tip (CNG-1): To'liq po'lat balon</b>
• Eng mustahkam va arzon
• Og'irligi: 70 — 95 kg (juda og'ir)
• Xizmat muddati: 15 yil

2️⃣ <b>2-Tip (CNG-2): Po'lat astar + shishatola</b>
• Po'lat silindr sirti kompozit tola bilan o'ralgan
• Og'irligi: 1-tipdan 20% yengilroq
• Narxi o'rtacha

3️⃣ <b>3-Tip (CNG-3): Alyuminiy astar + uglerod tolasi</b>
• Ichki qatlami yengil alyuminiy, sirti ugletola bilan to'liq mustahkamlangan
• Og'irligi: Po'latdan 45-50% yengil
• Mashina orqasini cho'ktirmaydi, lekin qimmatroq

4️⃣ <b>4-Tip (CNG-4): To'liq polimer kompozit</b>
• Po'lat mutlaqo yo'q! Ichki qismi polietilen, tashqarisi yuqori bosimli kompozit tola
• Korroziyaga (zangga) umuman uchramaydi
• Eng yengil va eng xavfsiz, narxi yuqori
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "toroid_info")
async def cb_toroid(call: CallbackQuery):
    text = """
🔘 <b>TOROID ("TABLETKA") PROPAN BALONLARI:</b>

• <b>Joylashuvi:</b> Avtomobilning zapas g'ildiragi (zapas baloni) o'rniga tushadi.
• <b>Hajmi:</b> Odatda 35, 42, 48, 54 litr bo'ladi.
• <b>Asosiy ustunligi:</b> Yukxonada (bagajda) joy zarracha ham kamaymaydi! Zapas g'ildirak uchun esa maxsus jildli chexol ishlatiladi.
• <b>Xavfsizlik:</b> Multiklapan balonning ichki markaziga joylashtiriladi va zarbalardan to'liq himoyalangan bo'ladi.
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "reduktor_freeze")
async def cb_reduktor_freeze(call: CallbackQuery):
    text = """
❄️ <b>REDUKTOR MUZLAB QOLGANDA TEZKOR YECHIMLAR:</b>

Agar reduktor ustini qor yoki oq qirov qoplasa:
1. <b>Harakatni darhol to'xtating va gazni o'chiring!</b> Muzlagan holatda gazda yurish reduktor membranasini yorib yuboradi.
2. <b>Ustiga qaynagan issiq suv quymang!</b> Haroratning keskin o'zgarishi korpusni yoki membranani yorishi mumkin.
3. <b>Antifriz idishini tekshiring:</b> Antifriz kam bo'lsa, yetarli darajada quying.
4. <b>Tizimdan havoni chiqaring:</b> Pechka yoki reduktorga kiruvchi shlangni ozgina bo'shatib, havoni (vozduh) chiqaring.
5. Mashinani faqat <b>benzinga</b> o'tkazib, motor 80-90°C ga yetguncha kuting, reduktor tabiiy isiydi.
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "reduktor_rem")
async def cb_reduktor_rem(call: CallbackQuery):
    text = """
🔄 <b>REDUKTOR REMKOMPLEKTINI ALMASHTIRISH:</b>

• <b>Qachon almashtiriladi?</b> Har 60 000 — 80 000 km dan keyin yoki reduktordan gaz hidi kelib, bosimni ushlay olmaganda.
• <b>Remkomplekt tarkibiga nimalar kiradi:</b>
  - Gaz bosimini boshqaruvchi elastik membranalar
  - Gazni to'suvchi rezina klapanlar
  - Antifriz o'tuvchi joylardagi issiqlikka chidamli halqalar (o-ring)
  - Filtrlash to'rlari
• <b>Eslatma:</b> Faqat original remkomplekt (masalan Tomasetto Original) o'rnating. Qalbaki (poddelka) membranalar qishki sovuqda tezda qotib, yorilib ketadi!
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "go_farsunka")
async def cb_go_farsunka(call: CallbackQuery):
    await call.message.answer(FARSUNKA_INFO, reply_markup=get_farsunka_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "farsunka_jiklir")
async def cb_farsunka_jiklir(call: CallbackQuery):
    text = """
⚙️ <b>JIKLIR DIAMETRINI ANIQLASH FORMULASI:</b>

Farsunka jiklirlarining diametri to'g'ri bo'lishi juda muhim:
• <b>Standart me'yor:</b> Gaz farsunkasining ochilish vaqti xolostoy yurishda <b>3.5 — 4.5 ms</b> (Valtek uchun) oralig'ida bo'lishi kerak.
• Agar vaqt <b>5.5 — 6.0 ms dan oshsa</b> ➔ Jiklir teshigi kichik, uni 0.2 mm ga kattalashtirish kerak.
• Agar vaqt <b>3.0 ms dan past bo'lsa</b> ➔ Jiklir juda katta, gaz haddan ko'p ketadi va dvigatel qaltiraydi.

Jiklirlarni faqat maxsus kalibrlangan sverlolar (0.1 mm qadamli) yordamida yo'nish lozim.
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "valtek_vs_barracuda")
async def cb_valtek_barracuda(call: CallbackQuery):
    text = """
⚡ <b>VALTEK 30 VA BARRACUDA TAQQOSLASH:</b>

┌─────────────────────┬─────────────────┬─────────────────┐
│ <b>Ko'rsatkich</b>        │ <b>Valtek Type 30</b> │ <b>Barracuda</b>       │
├─────────────────────┼─────────────────┼─────────────────┤
│ <b>Turi</b>               │ Porshenli       │ Ignali (injektor)│
│ <b>Ochilish vaqti</b>     │ 3.3 — 3.7 ms    │ <b>1.8 — 2.0 ms</b>   │
│ <b>Yopilish vaqti</b>     │ 2.2 — 2.8 ms    │ <b>1.2 ms</b>          │
│ <b>Shovqin darajasi</b>   │ Sezilarli ovoz  │ <b>Mutlaqo jim</b>     │
│ <b>Ta'mirlash</b>        │ Remkomplekt bor │ Almashtiriladi  │
│ <b>Xizmat muddati</b>    │ 40-60 ming km   │ <b>150+ ming km</b>    │
│ <b>Narxi</b>              │ Hamyonbop       │ O'rtacha/Qimmat │
└─────────────────────┴─────────────────┴─────────────────┘

💡 <b>Maslahat:</b> Cobalt, Lacetti va Gentra uchun Valtek ham, Barracuda ham yaxshi ishlaydi. Biroq zamonaviy xorijiy va turbomotorlar uchun Barracuda tavsiya qilinadi!
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "farsunka_noise")
async def cb_farsunka_noise(call: CallbackQuery):
    text = """
🛠 <b>FARSUNKA TAQILLASHINI (TOVUSHINI) YO'QOTISH:</b>

Valtek tipidagi farsunkalar 30-40 ming km dan so'ng dizel motoridek taqillab ishlashni boshlaydi:
1. <b>Sababi:</b> Porshenning pastki va yuqori zarba so'ndiruvchi rezina halqalari yassilanib, metall metallga tegadi.
2. <b>Yechimi:</b>
   • Farsunkaga remkomplekt (yangi shtok va rezinachalar) qo'yish.
   • <b>Mikrometr (soatli indikator)</b> yordamida shtok xodini aniq <b>0.45 mm</b> ga sozlash.
   • Noto'g'ri sozlangan farsunkada silindrlarga bir xil miqdorda gaz bormaydi, bu esa motor tebranishiga olib keladi.
"""
    await call.message.answer(text, reply_markup=get_back_inline(), parse_mode="HTML")
    await call.answer()

@router.callback_query(F.data == "back_home")
async def cb_back_home(call: CallbackQuery, state: FSMContext):
    await state.clear()
    user_name = call.from_user.first_name or "Haydovchi"
    text = WELCOME_TEXT.format(name=user_name)
    try:
        await call.message.edit_text(text, parse_mode="HTML")
    except Exception:
        await call.message.answer(text, reply_markup=get_main_keyboard(), parse_mode="HTML")
    await call.answer()

# ----------------- FOYDALANUVCHINING MATNLI SAVOLLARINI AI GA YUBORISH -----------------

@router.message(F.text)
async def handle_ai_user_question(message: Message):
    """
    Foydalanuvchi menyudagi tugmalardan tashqari har qanday savol yozganda:
    Sun'iy intellekt (Gemini AvtoGaz Usta) bilan bog'lanib professional javob qaytaradi.
    """
    user_text = message.text.strip()
    if not user_text:
        return

    # Avval "yozmoqda..." statusini chiqarish
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    # Gemini AI ustasiga murojaat qilish
    ai_response = await ask_ai_master(message.from_user.id, user_text)

    # Javobni yuborish (Markdown formatida yoki xato bo'lsa oddiy matnda)
    try:
        await message.answer(ai_response, reply_markup=get_ai_chat_inline(), parse_mode="Markdown")
    except TelegramBadRequest:
        await message.answer(ai_response, reply_markup=get_ai_chat_inline())
