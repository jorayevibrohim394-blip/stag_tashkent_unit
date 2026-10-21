"""
AvtoGaz Telegram boti uchun barcha tugmalar (Reply va Inline klaviaturalar)
"""
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Asosiy menyu Reply klaviaturasi"""
    keyboard = [
        [
            KeyboardButton(text="💬 AI Usta bilan suhbat")
        ],
        [
            KeyboardButton(text="⛽ Metan (CNG)"),
            KeyboardButton(text="🛢 Propan (LPG)")
        ],
        [
            KeyboardButton(text="⚖️ Metan vs Propan"),
            KeyboardButton(text="⚙️ Gaz Reduktori")
        ],
        [
            KeyboardButton(text="🔌 Gaz Farsunkalari"),
            KeyboardButton(text="🚗 GBO Avlodlari (2 va 4)")
        ],
        [
            KeyboardButton(text="🧯 Balonlar va Xavfsizlik"),
            KeyboardButton(text="🛠 Nosozliklar va Yechimlar")
        ],
        [
            KeyboardButton(text="💰 Tejash Kalkulyatori"),
            KeyboardButton(text="📞 Oltin Qoidalar")
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Kerakli bo'limni tanlang yoki savolingizni yozing..."
    )

def get_ai_chat_inline() -> InlineKeyboardMarkup:
    """AI Suhbatdosh uchun qulay amallar"""
    keyboard = [
        [
            InlineKeyboardButton(text="🗑 Suhbatni tozalash", callback_data="clear_ai_history"),
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_metan_inline() -> InlineKeyboardMarkup:
    """Metan bo'limi uchun qo'shimcha inline tugmalar"""
    keyboard = [
        [
            InlineKeyboardButton(text="⚖️ Propanga taqqoslash", callback_data="compare_gas"),
            InlineKeyboardButton(text="💰 Metanda tejash", callback_data="calc_quick")
        ],
        [
            InlineKeyboardButton(text="🧯 Metan balon turlari", callback_data="metan_cylinders"),
            InlineKeyboardButton(text="💬 AI Ustadan so'rash", callback_data="ask_ai_direct")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_propan_inline() -> InlineKeyboardMarkup:
    """Propan bo'limi uchun qo'shimcha inline tugmalar"""
    keyboard = [
        [
            InlineKeyboardButton(text="⚖️ Metanga taqqoslash", callback_data="compare_gas"),
            InlineKeyboardButton(text="💰 Propanda tejash", callback_data="calc_quick")
        ],
        [
            InlineKeyboardButton(text="🔘 Tabletka (Toroid) balon", callback_data="toroid_info"),
            InlineKeyboardButton(text="💬 AI Ustadan so'rash", callback_data="ask_ai_direct")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_reduktor_inline() -> InlineKeyboardMarkup:
    """Reduktor bo'limi inline tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="❄️ Reduktor muzlab qolsa...", callback_data="reduktor_freeze"),
            InlineKeyboardButton(text="🔄 Remkomplekt almashtirish", callback_data="reduktor_rem")
        ],
        [
            InlineKeyboardButton(text="🔌 Farsunkalarga o'tish", callback_data="go_farsunka"),
            InlineKeyboardButton(text="💬 AI Ustadan so'rash", callback_data="ask_ai_direct")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_farsunka_inline() -> InlineKeyboardMarkup:
    """Farsunka bo'limi inline tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="⚙️ Jiklir diametrlari", callback_data="farsunka_jiklir"),
            InlineKeyboardButton(text="⚡ Valtek vs Barracuda", callback_data="valtek_vs_barracuda")
        ],
        [
            InlineKeyboardButton(text="🛠 Taqillashni yo'qotish", callback_data="farsunka_noise"),
            InlineKeyboardButton(text="💬 AI Ustadan so'rash", callback_data="ask_ai_direct")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_calc_keyboard() -> InlineKeyboardMarkup:
    """Kalkulyator uchun tezkor tanlov tugmalari"""
    keyboard = [
        [
            InlineKeyboardButton(text="🔹 6 L / 100km (Spark)", callback_data="calc_val_6"),
            InlineKeyboardButton(text="🔹 7 L / 100km (Matiz)", callback_data="calc_val_7")
        ],
        [
            InlineKeyboardButton(text="🔹 8 L / 100km (Nexia)", callback_data="calc_val_8"),
            InlineKeyboardButton(text="🔹 9 L / 100km (Cobalt)", callback_data="calc_val_9")
        ],
        [
            InlineKeyboardButton(text="🔹 10 L / 100km (Gentra)", callback_data="calc_val_10"),
            InlineKeyboardButton(text="🔹 12 L / 100km (Malibu/K5)", callback_data="calc_val_12")
        ],
        [
            InlineKeyboardButton(text="🔹 14 L / 100km (Captiva/SUV)", callback_data="calc_val_14"),
            InlineKeyboardButton(text="✍️ Boshqa qiymat yozish", callback_data="calc_custom")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_back_inline() -> InlineKeyboardMarkup:
    """Faqat orqaga qaytish tugmasi"""
    keyboard = [
        [
            InlineKeyboardButton(text="💬 AI Ustadan so'rash", callback_data="ask_ai_direct"),
            InlineKeyboardButton(text="🔙 Bosh menyuga qaytish", callback_data="back_home")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
