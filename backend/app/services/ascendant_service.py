import swisseph as swe
from datetime import datetime
from app.services.planet_service import get_zodiac_sign
def get_ascendant(birth_date, birth_time, latitude, longitude):
    dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60.0)
    houses = swe.houses(jd, latitude, longitude, b'P')
    ascendant = houses[1][0]
    return {"longitude" : round(ascendant, 2), "sign" : get_zodiac_sign(ascendant)}
def get_houses(birth_date, birth_time, latitude, longitude):
    dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    jd = swe.julday(dt.year, dt.month,  dt.day, dt.hour + dt.minute / 60.0)
    houses = swe.houses(jd, latitude, longitude, b'P')
    cusps = houses[0]
    result = {}
    for i in range(12):
        result[f"House_{i+1}"] = round(cusps[i], 2)
    return result