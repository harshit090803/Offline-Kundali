import swisseph as swe
from datetime import datetime
from app.services.constants import (PLANETS, SIGNS, NAKSHATRAS)
from app.services.time_service import (local_to_utc)
from app.services.strength_service import (get_dignity, is_combust)
def get_zodiac_sign(longitude):
    sign_index = int(longitude // 30)
    return SIGNS[sign_index]
def get_nakshatra(longitude):
    nak_length = 360 / 27
    index = int(longitude // nak_length)
    return NAKSHATRAS[index]
def get_pada(longitude):
    nak_length = 360 / 27
    pada_length = nak_length / 4
    remainder = longitude % nak_length
    pada = int(remainder // pada_length) + 1
    return pada
def get_all_planets(birth_date: str, birth_time: str):
    utc_dt = local_to_utc(birth_date, birth_time, "Asia/Kolkata")
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
    result = {}
    for planet_name, planet_id in PLANETS.items():
        data = swe.calc_ut(jd, planet_id)
        longitude = data[0][0]
        speed = data[0][3]
        retrograde = speed < 0
        sign = get_zodiac_sign(longitude)
        result[planet_name] = {"longitude": round(longitude, 2), "sign": sign, "dignity": get_dignity(planet_name, sign, longitude), "nakshatra": get_nakshatra(longitude), "pada": get_pada(longitude), "retrograde": retrograde}
    sun_longitude = result["Sun"]["longitude"]
    rahu_longitude = result["Rahu"]["longitude"]
    ketu_longitude = (rahu_longitude + 180) % 360
    result["Ketu"] = {"longitude": round(ketu_longitude, 2), "sign": get_zodiac_sign(ketu_longitude), "dignity": get_dignity("Ketu", get_zodiac_sign(ketu_longitude), ketu_longitude), "nakshatra": get_nakshatra(ketu_longitude), "pada": get_pada(ketu_longitude), "retrograde": True}
    for planet_name in result:
        result[planet_name]["combust"] = is_combust(planet_name, result[planet_name]["longitude"], sun_longitude)
    return result