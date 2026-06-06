from pytz import utc
import swisseph as swe
from datetime import datetime
from app.services.planet_service import get_zodiac_sign
from app.services.time_service import (local_to_utc)
swe.set_sid_mode(swe.SIDM_LAHIRI)
def get_ascendant(birth_date, birth_time, latitude, longitude):
    utc_dt = local_to_utc(birth_date, birth_time, "Asia/Kolkata")
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
    houses = swe.houses(jd, latitude, longitude, b'P')
    ayanamsa = swe.get_ayanamsa(jd)
    ascendant = (houses[1][0] - ayanamsa) % 360
    return {"longitude" : round(ascendant, 2), "sign" : get_zodiac_sign(ascendant)}
def get_houses(birth_date, birth_time, latitude, longitude):
    utc_dt = local_to_utc(birth_date, birth_time, "Asia/Kolkata")
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)
    houses = swe.houses(jd, latitude, longitude, b'P')
    cusps = houses[0]
    result = {}
    for i in range(12):
        ayanamsa = swe.get_ayanamsa(jd)
        result[f"House_{i+1}"] = round((cusps[i] - ayanamsa) % 360, 2)
    return result