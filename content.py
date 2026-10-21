"""
AvtoGaz Telegram boti uchun barcha ma'lumotlar bazasi va matnlar
"""

WELCOME_TEXT = """
🚗💨 <b>Assalomu alaykum, {name}!</b>

<b>AvtoGaz Bot</b>ga xush kelibsiz! Ushbu bot avtomobillarga o'rnatiladigan gaz uskunalari (GBO) bo'yicha eng to'liq, ishonchli va professional ma'lumotlar to'plamidir.

Bu yerda siz:
• 💬 <b>AI Usta bilan suhbat:</b> Gaz bo'yicha har qanday savolingizni bering va professional javob oling!
• ⛽ <b>Metan (CNG)</b> va 🛢 <b>Propan (LPG)</b> haqida to'liq ma'lumot
• ⚖️ <b>Metan vs Propan:</b> qaysi biri sizga ma'qul?
• ⚙️ <b>Gaz Reduktori:</b> turlari, nosozliklari va sozlash
• 🔌 <b>Gaz Farsunkalari:</b> turlari, kalibrlash, tozalash
• 🚗 <b>GBO avlodlari:</b> 2-avlod va 4-avlod farqlari
• 🧯 <b>Gaz Balonlari va Xavfsizlik:</b> texnik ko'rik (opressovka)
• 🛠 <b>Nosozliklar va Yechimlar:</b> mashina siltansa, hid kelsa...
• 💰 <b>Yoqilg'i tejash kalkulyatori:</b> xarajatlarni aniq hisoblash

Pastdagi menyudan kerakli bo'limni tanlang yoki <b>to'g'ridan-to'g'ri gaz bo'yicha savolingizni yozib yuboring</b>: 👇
"""

AI_INTRO_TEXT = """
🤖 <b>AvtoGaz AI Usta bilan muloqot xonasi</b>

Assalomu alaykum! Men avtomobil gaz uskunalari (GBO) bo'yicha sun'iy intellekt ustasiman.

Sizga quyidagi masalalarda professional yordam bera olaman:
• 🚗 Mashinangizga qaysi gaz uskunasi (metan yoki propan) to'g'ri kelishi
• ⚙️ Reduktor va farsunkalar sozlamalari, jiklirlar tanlash
• 🛠 Gazda yurishdagi nosozliklar (siltanish, gaz hidi, ertalab kech o't olishi, gaz sarfi oshishi)
• 🧯 Balonlar xavfsizligi va texnik ko'rik talablari

⚠️ <b>DIQQAT:</b>
<i>Men faqat va faqat avtomobil gaz uskunalari (GBO) mavzusida yordam bera olaman. Mavzudan tashqari boshqa savollarga javob bera olmayman.</i>

Gaz tizimi bo'yicha o'zingizni qiziqtirgan savolni yozing: 👇
"""

HELP_TEXT = """
ℹ️ <b>AvtoGaz Botidan foydalanish qo'llanmasi:</b>

Bot orqali avtomobil gaz uskunalari haqida barcha bilimlarni olishingiz hamda professional AI usta bilan suhbatlashishingiz mumkin.

📌 <b>Asosiy buyruqlar:</b>
/start - Botni qayta ishga tushirish va bosh menyu
/ai yoki /chat - AI AvtoGaz Usta bilan suhbat
/clearchat - AI bilan suhbat tarixini tozalash
/kalkulyator - Yoqilg'i tejash kalkulyatori
/metan - Metan gazi haqida to'liq ma'lumot
/propan - Propan gazi haqida to'liq ma'lumot
/reduktor - Gaz reduktori haqida ma'lumot
/farsunka - Farsunkalar haqida ma'lumot
/taqqoslash - Metan va Propanni taqqoslash
/xavfsizlik - Xavfsizlik va balonlar qoidalari
/nosozliklar - Nosozliklar va yechimlar
/help - Ushbu yordam oynasi

💡 <b>Qulaylik:</b> Har qanday savolni botga to'g'ridan-to'g'ri matn ko'rinishida yozsangiz, AI Usta sizga professional javob qaytaradi!
"""

METAN_INFO = """
⛽ <b>METAN (CNG — Siqilgan Tabiiy Gaz) HAQIDA TO'LIQ MA'LUMOT</b>

<b>Metan (CNG) nima?</b>
Metan — bu asosan tabiiy gaz (CH₄) dan iborat bo'lib, maxsus kompressorlar yordamida juda yuqori bosim ostida (<b>200 - 250 atmosfera / bar</b>) avtomobil balloniga siqib to'ldiriladi.

━━━━━━━━━━━━━━━━━━━━
✅ <b>AFZALLIKLARI:</b>
1. <b>Eng arzon yoqilg'i:</b> Benzinga qaraganda 2.5 — 3 baravargacha iqtisodiy tejamkor.
2. <b>Dvigatel moyi uzoq xizmat qiladi:</b> Metan toza yonadi, qora kuya (nagar) hosil qilmaydi, motor moyi suyuqlashmaydi va toza turadi.
3. <b>Yuqori oktan soni:</b> Metanning oktan soni <b>105 - 110</b> ga teng. Bu esa detonatsiya (palts urishi) xavfini butunlay yo'qotadi.
4. <b>Ekologik toza:</b> Chiqindi gazlar ichida zaharli moddalar (CO, CH) benzinga nisbatan 60-70% kam.

━━━━━━━━━━━━━━━━━━━━
❌ <b>KAMCHILIKLARI:</b>
1. <b>Balonning og'irligi:</b> Standart temir balon (65-100 litr) taxminan <b>65 - 95 kg</b> tosh bosadi. Bu orqa podveskaga (prujina/amortizator) qo'shimcha yuk bo'ladi.
2. <b>Bagaj joyi qisqaradi:</b> Balon yukxonaning sezilarli qismini egallaydi.
3. <b>Masofa cheklanganligi:</b> Bir to'ldirishda o'rtacha <b>180 — 260 km</b> masofa bosib o'tadi.
4. <b>Zapravkalardagi navbatlar:</b> Qish mavsumida gaz bosimi tushishi va navbatlar kuzatilishi mumkin.
5. <b>Quvvat yo'qotishi:</b> Benzinga nisbatan motor quvvati 10-15% gacha kamayishi mumkin (ayniqsa variator qo'yilmagan bo'lsa).

━━━━━━━━━━━━━━━━━━━━
🧯 <b>METAN BALON TURLARI (TIP 1, 2, 3, 4):</b>
• <b>Tip 1 (To'liq po'lat):</b> Eng keng tarqalgan, arzon, mustahkam, lekin juda og'ir (70-90 kg).
• <b>Tip 2 (Po'lat + shishatola o'ram):</b> Og'irligi po'latga nisbatan 15-20% yengilroq.
• <b>Tip 3 (Alyuminiy korpus + uglerod tolasi):</b> Po'latdan 40-50% yengil, lekin narxi qimmat.
• <b>Tip 4 (To'liq polimer kompozit):</b> Eng yengil va zamonaviy, korroziyaga uchramaydi, narxi ancha yuqori.

━━━━━━━━━━━━━━━━━━━━
💡 <b>KIMLAR UCHUN TAVSIYA ETILADI?</b>
Kuniga 100 km dan ko'p yuradigan haydovchilar, taksi xizmati xodimlari, yuk tashuvchi tijoriy avtomobillar (Damas, Labo, Gazel va b.).
"""

PROPAN_INFO = """
🛢 <b>PROPAN (LPG — Suyultirilgan Neft Gazi) HAQIDA TO'LIQ MA'LUMOT</b>

<b>Propan (LPG) nima?</b>
Propan — bu neftni qayta ishlashdan olinadigan propan va butan gazlarining aralashmasidir. U past bosimda (<b>10 — 16 atmosfera / bar</b>) suyuq holatga aylanadi va suyuqlik sifatida saqlanadi.

━━━━━━━━━━━━━━━━━━━━
✅ <b>AFZALLIKLARI:</b>
1. <b>Past bosim va yuqori xavfsizlik:</b> Balondagi bosim atigi 10-16 bar (metandagi 200 bardan 15 barobar kam).
2. <b>Yengil balonlar:</b> Balon og'irligi atigi <b>20 — 30 kg</b> bo'lib, avtomobil podveskasiga deyarli ortiqcha yuk bermaydi.
3. <b>Toroid (Zapaska o'rniga "Tabletka") balon:</b> Balonni zapas g'ildirak o'rniga o'rnatish mumkin, natijada yukxona (bagaj) butunlay bo'sh qoladi!
4. <b>Katta masofa:</b> Bir to'liq zapravkada <b>400 — 600 km</b> masofa bosib o'tish mumkin.
5. <b>Dvigatel quvvati deyarli yo'qolmaydi:</b> Benzinga nisbatan yo'qotish bor-yo'g'i 3-5% ni tashkil qiladi.
6. <b>Navbatlar yo'q:</b> Propan zapravkalarda navbatlar deyarli uchramaydi, quyish vaqti 2-3 daqiqa.

━━━━━━━━━━━━━━━━━━━━
❌ <b>KAMCHILIKLARI:</b>
1. <b>Narxi metandan biroz qimmatroq:</b> Benzinga nisbatan ancha arzon bo'lsa-da, metanchalik tejamkor emas.
2. <b>Haroratga bog'liqlik:</b> Qishda va yozda propan va butan nisbati to'g'ri bo'lishi kerak (qishda propan ulushi ko'p bo'lishi lozim).
3. <b>Odorant hidi:</b> Kichik gaz qochishi bo'lsa ham hidi kuchli seziladi (chunki propan havodan og'ir va pastga cho'kadi).

━━━━━━━━━━━━━━━━━━━━
🧯 <b>BALON TURLARI:</b>
• <b>Toroid balon (Tabletka):</b> Zapas g'ildirak o'rniga tushadi (35-54 litr). Bagaj toza qoladi.
• <b>Silindrsimon balon:</b> Yukxonaga o'rnatiladi (50-90 litr), uzoq yo'lga yuruvchilar uchun mos.

━━━━━━━━━━━━━━━━━━━━
💡 <b>KIMLAR UCHUN TAVSIYA ETILADI?</b>
Shaxsiy avtomobil egalari, uzoq viloyatlararo qatnaydiganlar, yangi xorijiy avtomobillar egalari (Chevrolet Tracker, Onix, Gentra, Kia, Hyundai) hamda bagaj joyi muhim bo'lgan oilalar.
"""

TAQQOSLASH_TEXT = """
⚖️ <b>METAN VA PROPAN TAQQOSLASH JADVALI</b>

Quyidagi jadval orqali o'zingizga qaysi yoqilg'i turi mos kelishini aniqlang:

┌──────────────────────┬─────────────────┬─────────────────┐
│ <b>Ko'rsatkich</b>         │ <b>Metan (CNG)</b>     │ <b>Propan (LPG)</b>    │
├──────────────────────┼─────────────────┼─────────────────┤
│ <b>Bosimi</b>               │ 200 — 250 bar   │ 10 — 16 bar     │
│ <b>Holati</b>               │ Siqilgan gaz    │ Suyultirilgan   │
│ <b>Balon og'irligi</b>      │ 65 — 95 kg      │ 20 — 30 kg      │
│ <b>1 zapravkada yurish</b>  │ 180 — 260 km    │ 400 — 600 km    │
│ <b>Yukxona (bagaj)</b>      │ 40-60% egallaydi│ Bo'sh (tabletka)│
│ <b>Tejamkorlik</b>          │ Maksimal (eng arzon)│ O'rta (benzinga nisbatan arzon) │
│ <b>Motor quvvati</b>        │ -10% ... -15%   │ -3% ... -5%     │
│ <b>Zapravkadagi navbat</b>  │ Tez-tez navbat  │ Navbat yo'q     │
│ <b>Qishki barqarorlik</b>   │ Bosim tushishi  │ Barqaror        │
│ <b>Havoga nisbatan</b>      │ Havodan yengil  │ Havodan og'ir   │
└──────────────────────┴─────────────────┴─────────────────┘

🎯 <b>XULOSA:</b>
• Agar siz <b>taksi haydasangiz</b>, kuniga 150-300 km yursangiz va <b>eng ko'p pul tejash</b> asosiy maqsadingiz bo'lsa — <b>METAN</b> tanlang!
• Agar siz mashinani <b>oilaviy ishlatsangiz</b>, yukxona kerak bo'lsa, uzoq safarlarga chiqsangiz va <b>zapravkada vaqt yo'qotishni istamasangiz</b> — <b>PROPAN</b> tanlang!
"""

REDUKTOR_INFO = """
⚙️ <b>GAZ REDUKTORI BO'YICHA TO'LIQ QO'LLANMA</b>

<b>Gaz reduktori nima va nima uchun kerak?</b>
Reduktor — bu avtogaz uskunasining "yuragi" hisoblanadi. Uning ikkita asosiy vazifasi bor:
1. <b>Bosimni pasaytirish:</b> Balondan kelayotgan yuqori bosimli gazni (metanda 200 bar, propanda 16 bar) dvigatel uchun mos bo'lgan <b>1.0 — 1.5 bar</b> ishchi bosimga tushirib beradi.
2. <b>Gazni bug'latish:</b> Suyuq propan yoki siqilgan metan kengayganda harorat keskin pasayadi (fizika qonunlariga ko'ra <b>-40°C gacha</b> muzlaydi). Gaz muzlab qolmasligi uchun reduktor korpusi orqali dvigatelning issiq <b>antifrizi</b> aylanib turadi.

━━━━━━━━━━━━━━━━━━━━
🏆 <b>MASHHUR REDUKTOR BRENDLARI:</b>
• <b>Tomasetto (Italiya):</b> Dunyoda va O'zbekistonda eng ommabop. AT09 Alaska (136 ot kuchigacha), Nordic (170 ot kuchi), Artic (240 ot kuchi). Ishonchli, ta'mirlash oson.
• <b>Lovato (Italiya):</b> Yuqori sifat, barqaror bosim ushlashi bilan mashhur.
• <b>Atiker (Turkiya):</b> Hamyonbop va sifatli variant, ehtiyot qismlari arzon.
• <b>KME / BRC / Romano:</b> Yuqori quvvatli (turbovali va 6-8 silindrli) motorlar uchun professional yechimlar.

━━━━━━━━━━━━━━━━━━━━
⚠️ <b>REDUKTORNING ASOSIY NOSOZLIKLARI VA BELGILARI:</b>

1. <b>Reduktor muzlab qolishi (oq qor bosishi):</b>
   • <i>Sababi:</i> Sovutish suyuqligi (antifriz) sathi kamaygan, shlanglarda havo tiqilib qolgan (vozduh), termostat ishlamayapti yoki reduktor radiator balandligidan teparoqqa noto'g'ri o'rnatilgan.
   • <i>Xavfi:</i> Membranalar yoriladi, mashina to'xtaydi.

2. <b>Gazdan benzinga o'z-o'zidan o'tib ketishi:</b>
   • <i>Sababi:</i> Reduktor gaz bosimini ushlay olmayapti, suyuq faza filtri tiqilib qolgan yoki reduktor ichidagi differensial klapan yeyilgan.

3. <b>Ertalab mashina qiyin o't olishi (starter uzoq aylanadi):</b>
   • <i>Sababi:</i> Reduktorning vakuum shlangi orqali gaz dvigatel kollektoriga sekin sizib o'tgan. Tunda kollektor gazga to'ladi va ertalab benzin bilan birga aralashib, shamchalarni (svechalarni) namlab qo'yadi.

4. <b>Reduktordan gaz hidi kelishi:</b>
   • <i>Sababi:</i> Membrana eskirgan, yorilgan yoki qotib qolgan. Qistirmalar (prokladkalar) zichligini yo'qotgan.

━━━━━━━━━━━━━━━━━━━━
🛠 <b>TEXNIK XIZMAT KO'RSATISH VA MASLAHATLAR:</b>
• Har <b>8 000 — 10 000 km</b> da suyuq faza filtrini almashtiring!
• Har <b>60 000 — 80 000 km</b> da reduktorga <b>remkomplekt</b> (yangi membranalar va klapanlar) qo'ying yoki yangisiga almashtiring.
• Qishda mashina motori kamida <b>40-50°C</b> ga qizimasdan turib gazga o'tkazmang (4-avlod buni avtomatik qiladi).
"""

FARSUNKA_INFO = """
🔌 <b>GAZ FARSUNKALARI (INJEKTORLAR) HAQIDA TO'LIQ MA'LUMOT</b>

<b>Gaz farsunkasi nima?</b>
4-avlod GBO da gaz farsunkalari har bir silindrga alohida o'rnatiladi. Ular elektron boshqaruv bloki (ECU) buyrug'i bilan mikrosekundlar (ms) ichida ochilib-yopilib, gazni to'g'ridan-to'g'ri dvigatel qabul qilish klapanlariga purkab beradi.

━━━━━━━━━━━━━━━━━━━━
📊 <b>FARSUNKA TURLARI VA SOLISHTIRISH:</b>

1. <b>Valtek Type 30 (3 Ohm) — Budjet klass:</b>
   • <i>Xususiyati:</i> Eng arzon va keng tarqalgan farsunka. Ta'mirlash oson (remkomplekti bor).
   • <i>Ochilish vaqti:</i> ~3.3 ms (nisbatan sekin).
   • <i>Kamchiligi:</i> 30-40 ming km dan keyin ovozi balandlashadi ("taq-taq" qiladi), kalibrlash talab etadi.

2. <b>Barracuda / Hana / Romano — Premium klass:</b>
   • <i>Xususiyati:</i> Ignasimon (porshenli emas) yuqori tezlikdagi farsunkalar. Benzin injektorlari bilan bir xil tezlikda ishlaydi.
   • <i>Ochilish vaqti:</i> <b>1.8 — 2.0 ms</b> (juda tez!).
   • <i>Afzalligi:</i> Jim ishlaydi, sovuqda qotmaydi, 150 000 km dan ortiq xizmat qiladi.
   • <i>Tavsiya:</i> Zamonaviy Yevropa, Yaponiya va Koreya mashinalari uchun eng to'g'ri tanlov.

3. <b>AEB / OMVL:</b>
   • Tezyurar membranali farsunkalar, o'rta narx toifasi, uzoq xizmat qiladi.

━━━━━━━━━━━━━━━━━━━━
🎯 <b>JIKLIRLARNI KALIBRLASH (DIAMETRNI TO'G'RI TANLASH):</b>
Farsunka uchiga o'rnatiladigan jiklirlar motor hajmi va quvvatiga qarab maxsus drel bilan yo'niladi (sverlit qilinadi):
• 1.2 — 1.4 litr motorlar uchun: <b>1.6 — 1.8 mm</b>
• 1.5 — 1.6 litr motorlar uchun (Nexia, Cobalt, Lacetti): <b>1.9 — 2.1 mm</b>
• 1.8 — 2.0 litr motorlar uchun: <b>2.2 — 2.4 mm</b>
• 2.4+ litr yoki turbovali motorlar uchun: <b>2.5 mm va undan yuqori</b>

<i>Eslatma:</i> Agar jiklir kichik yo'nilsa — mashina yuqori tezlikda tortmaydi, gaz farsunka vaqti me'yordan oshib ketadi. Agar juda katta yo'nilsa — dvigatel xolostoy yurishda tebranadi (silkinadi) va gaz hidi keladi.

━━━━━━━━━━━━━━━━━━━━
⚠️ <b>FARSUNKA NOSOZLIKLARI BELGILARI:</b>
1. <b>Dvigatel silkinishi (Troit qilish):</b> Birorta farsunka to'liq ochilmayapti yoki tiqilib qolgan.
2. <b>Qattiq taqillagan ovoz:</b> Farsunka porshenining rezina zarba so'ndiruvchisi yeyilgan (mikrometr yordamida shtok xodi sozlanishi kerak).
3. <b>Mashina siltanishi (proval):</b> Farsunkalarning ochilish tezligi benzin injektoriga mos kelmayapti.

━━━━━━━━━━━━━━━━━━━━
🧹 <b>TOZALASH VA PARVARISHLASH:</b>
• Gaz sifatiga bog'liq ravishda har <b>30 000 — 40 000 km</b> da farsunkalarni maxsus stendda yuvish tavsiya etiladi.
• Bug' faza filtrini (parovoy filtr) har <b>8 000 — 10 000 km</b> da almashtirish farsunkalar umrini 2-3 barobar uzaytiradi!
"""

GBO_AVLODLARI = """
🚗 <b>GBO (GAZ USKUNALARI) AVLODLARI: 2-AVLOD VA 4-AVLOD FARQI</b>

Hozirgi kunda O'zbekiston yo'llarida asosan 2-avlod va 4-avlod gaz uskunalari ishlatiladi:

━━━━━━━━━━━━━━━━━━━━
🔷 <b>2-AVLOD (Oddiy karbyurator va oddiy injektorlar uchun):</b>
• <i>Ishlash prinsipi:</i> Gaz reduktordan chiqib, bitta shlang orqali havo filtridan keyin qo'yilgan aralashtirgichga (smesitel/chashka) keladi. Sozlash qo'lda burab (dozator orqali) amalga oshiriladi.
• <i>Mos keladi:</i> VAZ (Jiguli), Damas, Nexia 1 (SOHC), Matiz, eski karbyuratorli mashinalar.
• <i>Kamchiliklari:</i>
  - <b>"Xlopok" (Paqillash):</b> Havo kollektorida gaz to'planib, shamcha uchqunidan paqillab portlashi va havo filtrini yorib yuborishi mumkin.
  - Yoqilg'i sarfi nisbatan ko'proq.
  - Quvvat sezilarli pasayadi (15-20%).

━━━━━━━━━━━━━━━━━━━━
🔶 <b>4-AVLOD (Taqsimlangan elektron purkash — zamonaviy standart):</b>
• <i>Ishlash prinsipi:</i> Har bir silindr uchun alohida gaz farsunkasi o'rnatiladi. Tizimni mikroprotsessorli Gaz ECU (kompyuter), MAP datchik, gaz harorati va bosim datchiklari boshqaradi.
• <i>Mos keladi:</i> Cobalt, Gentra, Nexia 3, Tracker, Malibu, Onix, barcha zamonaviy xorijiy avtomobillar.
• <i>Afzalliklari:</i>
  - <b>Paqillash mutlaqo yo'q!</b> Gaz faqat klapan ochilganda silindr ichiga purkaladi.
  - Avtomatik ravishda benzinga va gazga o'tish (motor qiziganda gazga o'tadi, gaz tugasa o'zi benzinga o'tadi).
  - Quvvat deyarli yo'qolmaydi, tejamkorlik yuqori.
  - Diagnostika kompyuter orqali aniq sozlanadi.

━━━━━━━━━━━━━━━━━━━━
🚀 <b>5 VA 6-AVLOD (To'g'ridan-to'g'ri purkash — GDI, TSI, TFSI):</b>
• Gaz suyuq holatda yuqori bosimli nasos orqali to'g'ridan-to'g'ri silindrga purkaladi. Reduktor talab qilinmaydi. Narxi qimmat bo'lgani sababli kam uchraydi.
"""

XAVFSIZLIK_BALONLAR = """
🧯 <b>GAZ BALONLARI VA XAVFSIZLIK QOIDALARI</b>

Gaz bilan jihozlangan avtomobildan xavfsiz foydalanish uchun quyidagi qoidalarga qat'iy amal qilish shart:

━━━━━━━━━━━━━━━━━━━━
📋 <b>1. TEXNIK KO'RIK (OPRESSOVKA) MUDDATLARI:</b>
• <b>Metan balonlar:</b> Har <b>3 yilda</b> maxsus litsenziyaga ega laboratoriyalarda <b>300 atmosfera</b> suv bosimi ostida tekshiruvdan (opressovka) o'tishi va dalolatnoma olinishi shart!
• <b>Propan balonlar:</b> Har <b>2 yilda</b> bir marta sinovdan o'tkaziladi.
• <i>Eslatma:</i> Balonning maksimal foydalanish muddati odatda ishlab chiqarilgan kundan boshlab <b>15 yil</b>! Muddati o'tgan balondan foydalanish qat'iyan taqiqlanadi!

━━━━━━━━━━━━━━━━━━━━
🛡 <b>2. MULTIKLAPAN VA XAVFSIZLIK KLAPANLARI:</b>
Zamonaviy GBO tizimlarida xavfsizlik uchun quyidagi himoya mexanizmlari mavjud:
1. <b>Ortiqcha bosim klapani (PRV):</b> Yozda issiqda balondagi bosim haddan tashqari oshib ketsa, gazni tashqariga sekin chiqarib, portlashning oldini oladi.
2. <b>Tezkor uzish klapani:</b> Trubka uzilib ketsa yoki avariya bo'lsa, gazning shiddat bilan otilib chiqishini bir zumda to'xtatadi.
3. <b>Elektromagnit klapan:</b> Dvigatel o'chirilganda gaz trubkasini avtomatik berkitaradi.

━━━━━━━━━━━━━━━━━━━━
⛽ <b>3. ZAPRAVKA VAQTIDAGI QOIDALAR:</b>
• Gaz quyishdan oldin barcha <b>yo'lovchilarni mashinadan tushiring</b>!
• Dvigatelni va barcha chiroqlarni o'chiring.
• <b>Propan uchun 80% qoidasi:</b> Propan baloniga uning hajmidan 80% dan ko'p gaz quymaslik kerak! (Qolgan 20% bo'sh joy issiqda gazning kengayishi uchun xavfsizlik buferidir).
• Metanda ruxsat etilgan bosim <b>200 bar</b> (20 MPa).

━━━━━━━━━━━━━━━━━━━━
🚨 <b>4. GAZ HIDI KELGANDA NIMA QILISH KERAK?</b>
1. Darhol avtomobilni xavfsiz joyda to'xtating va dvigatelni o'chiring.
2. Bagajni ochib, balon ustidagi <b>mexanik ventillarni qo'lda to'liq yoping</b>!
3. Eshik va oynalarni ochib, salonni yaxshilab shamollating.
4. Hech qanday elektr tugmalarni yoqmang, zajiganiyeni buramang va chekmang!
5. Mashinani evakuatorda yoki faqat benzinga o'tkazgan holda GBO servisiga olib boring.
"""

NOSOZLIKLAR_YECHIMLAR = """
🛠 <b>GBO DA ENG KO'P UCHRAYDIGAN 8 TA MUAMMO VA ULARNING YECHIMI</b>

1. <b>Mashina gazda tortmaydi yoki siltanadi:</b>
   • <i>Sabab 1:</i> Shamchalar (svecha) yoki yuqori kuchlanish simlari (provod) eskirgan. Gaz aralashmasini yondirish uchun benzinga qaraganda 2 barobar kuchliroq uchqun talab qilinadi.
   • <i>Sabab 2:</i> Gaz filtrlari ifloslangan.
   • <i>Yechim:</i> Svechalarni yangilang (gaz uchun svecha oraliq masofasi 0.7 - 0.8 mm bo'lishi ma'qul) va gaz filtrlarini almashtiring.

2. <b>Gazdan o'z-o'zidan benzinga o'tib ketadi:</b>
   • <i>Sabab:</i> Gaz bosimi datchigi (MAP) bosim pasayganini ko'rsatmoqda, reduktor qizimagan yoki suyuq faza filtri butunlay tiqilib qolgan.
   • <i>Yechim:</i> Reduktor haroratini tekshiring, gaz filtrlarini almashtiring.

3. <b>Gaz sarfi me'yordan oshib ketdi:</b>
   • <i>Sabab:</i> Gaz xaritasi (kalibrovka) buzilgan, reduktor bosimi haddan tashqari ko'tarilgan, farsunka jiklirlari haddan tashqari katta yoki havo datchigi (lyambda-zond) nosoz.
   • <i>Yechim:</i> Kompyuter diagnostikasi qilib, gaz xaritasini qayta sozlatish (avtokalibrovka va yo'lda xarita chizish).

4. <b>Ertalab dvigatel kech yoki zo'rg'a o't oladi:</b>
   • <i>Sabab:</i> Reduktor membranasi yirtilgan yoki gaz farsunkalari zich yopilmayapti. Natijada kechasi bilan gaz kollektorga sizib, ertalab benzin bilan birga dvigatelni "bo'g'ib" qo'yadi.
   • <i>Tekshirish:</i> Kechasi reduktorning vakuum shlangini yechib, bir stakan suvga solib qo'ying. Agar pufakchalar chiqsa — reduktor teshilgan!

5. <b>Salonga gaz hidi kirishi:</b>
   • <i>Sabab:</i> Shlang xomutlari bo'shagan, reduktor yoki farsunka ulanish joylari zich emas, yoki gaz to'liq yonmayapti.
   • <i>Yechim:</i> Sovunli ko'pik yordamida barcha birikmalarni tekshirib, xomutlarni torting.

6. <b>Reduktor muzlab qor bosib qolishi:</b>
   • <i>Sabab:</i> Antifriz aylanmayapti, sistema ichida havo tiqilib qolgan yoki antifriz sathi yetarli emas.
   • <i>Yechim:</i> Antifriz quying, tizimdagi havoni chiqaring.

7. <b>Farsunkalar qattiq taqillab ishlayapti:</b>
   • <i>Sabab:</i> Farsunka rezinalari yeyilgan, shtok xodi kattalashgan.
   • <i>Yechim:</i> Mikrometr bilan shtok xodini (0.45 - 0.50 mm) qilib sozlash yoki remkomplekt almashtirish.

8. <b>"Check Engine" chirog'i yonishi:</b>
   • <i>Sabab:</i> "Kambag'al aralashma" (Бедная смесь - P0171) xatosi. Gaz yetishmayapti, klapanlar kuyish xavfi bor.
   • <i>Yechim:</i> Zudlik bilan gaz ustasiga borib, aralashmani to'g'rilash lozim.
"""

TAVSIYALAR_VA_QOIDALAR = """
📞 <b>GAZDA YURADIGAN HAYDOVCHILAR UCHUN OLTIN QOIDALAR</b>

Dvigatelingiz uzoq va muammosiz xizmat qilishi uchun quyidagi tavsiyalarga amal qiling:

1. <b>Har doim bakda kamida 10-15 litr benzin saqlang!</b>
   Benzonasos (yoqilg'i nasosi) benzin ichida sovib turadi. Agar bakda benzin kam bo'lsa, nasos qizib, tezda kuyib qoladi.

2. <b>Har 10 000 km da gaz filtrlarini almashtiring!</b>
   Filtrlar arzon turadi, lekin ularni vaqtida almashtirmaslik qimmatbaho reduktor va farsunkalarni ishdan chiqaradi.

3. <b>Har 300-400 km gazda yurgandan so'ng, kamida 20-30 km benzin bilan yuring!</b>
   Bu klapanlar va benzin injektorlarining tozalanishini hamda qizib ketmasligini ta'minlaydi.

4. <b>Shamchalarni (svechalarni) har 20 000 — 30 000 km da yangilang!</b>
   Eski svechalar gazda bobinalarni (katushka zajiganiya) tezda kuydiradi.

5. <b>Klapanlar oralig'ini (zazorlarini) nazorat qiling!</b>
   Gidrokompensatori yo'q dvigatellarda (masalan Nexia 1.5, Damas, Cobalt, ayrim Hyundai/Kia modellari) har 30 000 - 40 000 km da klapanlar sozlanishi (regulirovka) shart, aks holda gaz yuqori haroratda klapanlarni kuydirib yuborishi mumkin.
"""

KALKULYATOR_EXPLAIN = """
💰 <b>YOQILG'I TEJAMKORLIGI KALKULYATORI</b>

Ushbu kalkulyator yordamida siz benzin, propan va metan xarajatlarini hamda gaz o'rnatish orqali qancha pul tejashingizni aniq bilib olasiz!

Hozirgi o'rtacha narxlar asosida hisoblanadi:
• 🛢 Benzin (AI-92): <b>{benzin_price:,} so'm / litr</b>
• ⛽ Metan (CNG): <b>{metan_price:,} so'm / m³</b>
• 🚗 Propan (LPG): <b>{propan_price:,} so'm / litr</b>

Pastdagi tugmalardan avtomobilingizning <b>100 km uchun o'rtacha benzin sarfini</b> tanlang yoki o'zingiz istagan raqamni yozib yuboring (masalan: <code>8.5</code>): 👇
"""
