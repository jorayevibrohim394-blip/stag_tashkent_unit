"""
Yoqilg'i sarfi va tejash kalkulyatori
"""
from config import PRICE_BENZIN_AI92, PRICE_METAN, PRICE_PROPAN

def calculate_fuel_economy(benzin_consumption: float) -> str:
    """
    100 km va 10 000 km uchun Benzin, Metan va Propan xarajatlari hamda
    tejamkorlikni hisoblab chiroyli matn shaklida qaytaradi.
    """
    # 100 km uchun miqdorlar
    b_liters_100 = benzin_consumption
    m_cubes_100 = round(benzin_consumption * 0.95, 1)    # 1 litr benzin ~ 0.95 m3 metan
    p_liters_100 = round(benzin_consumption * 1.18, 1)   # 1 litr benzin ~ 1.18 L propan

    # 100 km xarajatlari (so'mda)
    cost_b_100 = int(b_liters_100 * PRICE_BENZIN_AI92)
    cost_m_100 = int(m_cubes_100 * PRICE_METAN)
    cost_p_100 = int(p_liters_100 * PRICE_PROPAN)

    # 10 000 km xarajatlari (so'mda)
    cost_b_10k = cost_b_100 * 100
    cost_m_10k = cost_m_100 * 100
    cost_p_10k = cost_p_100 * 100

    # 10 000 km da tejaladigan pul
    savings_metan = cost_b_10k - cost_m_10k
    savings_propan = cost_b_10k - cost_p_10k

    result = f"""
📊 <b>YOQILG'I SARFI HISOB-KITOBI (100 km ga {benzin_consumption} L benzin misolida):</b>

━━━━━━━━━━━━━━━━━━━━
⛽ <b>100 KM MASOFA UCHUN:</b>
• 🛢 <b>Benzin:</b> {b_liters_100} L ➔ <b>{cost_b_100:,} so'm</b>
• ⛽ <b>Metan:</b> {m_cubes_100} m³ ➔ <b>{cost_m_100:,} so'm</b>
• 🚗 <b>Propan:</b> {p_liters_100} L ➔ <b>{cost_p_100:,} so'm</b>

━━━━━━━━━━━━━━━━━━━━
🛣 <b>10 000 KM YURGANDA (O'rtacha 3-6 oylik yurish):</b>
• 🛢 <b>Benzin:</b> {cost_b_10k:,} so'm
• ⛽ <b>Metan:</b> {cost_m_10k:,} so'm
• 🚗 <b>Propan:</b> {cost_p_10k:,} so'm

━━━━━━━━━━━━━━━━━━━━
💰 <b>SIZNING CHO'NTAGINGIZDA QOLADIGAN SOF FOYDA (TEJAM):</b>
• 🟢 <b>Metanda yursangiz:</b>
  10 000 km da ➔ <b>+{savings_metan:,} so'm</b> tejaladi!
  <i>(Benzinga qaraganda deyarli 3 barobar arzon!)</i>

• 🔵 <b>Propanda yursangiz:</b>
  10 000 km da ➔ <b>+{savings_propan:,} so'm</b> tejaladi!
  <i>(Benzinga qaraganda qariyb 40% arzonroq va qulay!)</i>

━━━━━━━━━━━━━━━━━━━━
<i>Hisob-kitob AI-92 ({PRICE_BENZIN_AI92:,} so'm), Metan ({PRICE_METAN:,} so'm/m³) va Propan ({PRICE_PROPAN:,} so'm/L) o'rtacha narxlariga asoslangan.</i>
"""
    return result.strip()
