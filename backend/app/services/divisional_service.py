from app.services.planet_service import get_zodiac_sign
def get_d2_sign(longitude):
    sign_index = int(longitude // 30)
    degree_in_sign = longitude % 30
    odd_signs = [0, 2, 4, 6, 8, 10]
    if sign_index in odd_signs:
        if degree_in_sign < 15:
            return "Leo"
        else:
            return "Cancer"
    else:
        if degree_in_sign < 15:
            return "Cancer"
        else:
            return "Leo"
def get_d2_chart(planets):
    result ={}
    for planet_name, data in planets.items():
        longitude = data["longitude"]
        result[planet_name] = {"d2_sign" : get_d2_sign(longitude)}
    return result
SIGNS = [
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
MOVABLE_SIGNS = [
    "Aries",
    "Cancer",
    "Libra",
    "Capricorn"
]
FIXED_SIGNS = [
    "Taurus",
    "Leo",
    "Scorpio",
    "Aquarius"
]
DUAL_SIGNS = [
    "Gemini",
    "Virgo",
    "Sagittarius",
    "Pisces"
]
def get_d3_sign(longitude):
    sign_index = int(longitude // 30)
    degree_in_sign = longitude % 30
    drekkana = int(degree_in_sign // 10)
    if drekkana == 0:
        return SIGNS[sign_index]
    elif drekkana == 1:
        return SIGNS[(sign_index + 4) % 12]
    else:
        return SIGNS[(sign_index + 8) % 12]
def get_d3_chart(planets):
    result = {}
    for planet_name, data in planets.items():
        longitude = data["longitude"]
        result[planet_name] = {"d3_sign" : get_d3_sign(longitude)}
    return result
def get_d9_sign(longitude):
    sign_index = int(longitude // 30)
    sign = SIGNS[sign_index]
    degree_in_sign = longitude % 30
    navamsha_number = int(degree_in_sign // (30 / 9))
    if sign in MOVABLE_SIGNS:
        start_index = sign_index
    elif sign in FIXED_SIGNS:    
        start_index = (sign_index + 8) % 12
    else:
        start_index = (sign_index + 4) % 12   
    destination_sign = (start_index + navamsha_number) % 12
    return SIGNS[destination_sign]
def get_d9_chart(planets):
    result = {}
    for planet_name, data in planets.items():
        longitude = data["longitude"]
        result[planet_name] = {"d9_sign" : get_d9_sign(longitude)}
    return result
def get_d10_chart(planets):
    pass
def get_d12_chart(planets):
    pass
def get_d16_chart(planets):
    pass
def get_d24_chart(planets):
    pass
def get_d27_chart(planets):
    pass
def get_d30_chart(planets):
    pass