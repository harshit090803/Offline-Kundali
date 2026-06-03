import swisseph as swe
from datetime import datetime
from app.services.constants import PLANETS  
from app.services.constants import NAKSHATRAS
def get_sun_position(
    birth_date : str,
    birth_time : str
):
    dt = datetime.strptime(
        f"{birth_date} {birth_time}",
        "%Y-%m-%d %H:%M"
    )
    jd = swe.julday(
        dt.year,
        dt.month,
        dt.day,
        dt.hour + dt.minute / 60.0
    )
    sun_data = swe.calc_ut(
        jd,
        swe.SUN
    )
    longitude = sun_data[0][0]
    return {
        "planet" : "Sun",
        "longitude" : longitude,
        "sign" : get_zodiac_sign(longitude)
    }
def get_zodiac_sign(longitude):
    signs = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces"
    ]
    sign_index = int(longitude // 30)
    return signs[sign_index]
def get_all_planets(
    birth_date: str,
    birth_time: str
):

    dt = datetime.strptime(
        f"{birth_date} {birth_time}",
        "%Y-%m-%d %H:%M"
    )

    jd = swe.julday(
        dt.year,
        dt.month,
        dt.day,
        dt.hour + dt.minute / 60
    )

    result = {}

    for planet_name, planet_id in PLANETS.items():

        data = swe.calc_ut(
            jd,
            planet_id
        )

        longitude = data[0][0]

        result[planet_name] = {
            "longitude": round(longitude, 2),
            "sign": get_zodiac_sign(longitude),
            "nakshatra" : get_nakshatra(longitude),
            "pada" : get_pada(longitude)
        }

    return result
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