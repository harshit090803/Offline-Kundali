from app.services.planet_service import get_zodiac_sign
from app.services.constants import SIGNS, MOVABLE_SIGNS, FIXED_SIGNS, DUAL_SIGNS, ODD_SIGNS, FIRE_SIGNS, EARTH_SIGNS, AIR_SIGNS, WATER_SIGNS
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
def get_d4_sign(longitude):
    sign_index = int(longitude // 30)
    degree_in_sign = longitude % 30
    chaturthamsha_number = int(degree_in_sign // 7.5)
    destination_index = (sign_index + (chaturthamsha_number * 3)) % 12
    return SIGNS[destination_index]
def get_d4_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d4_sign" : get_d4_sign(longitude)}
    return result
def get_d7_sign(longitude):
    sign_index = int(longitude // 30)
    sign = SIGNS[sign_index]
    degree_in_sign = longitude % 30
    saptamsha_number = int(degree_in_sign // (30 / 7))
    if sign_index % 2 == 0:
        start_index = sign_index
    else:
        start_index = (sign_index + 6) % 12
    destination_index = (start_index + saptamsha_number) % 12
    return SIGNS[destination_index]
def get_d7_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d7_sign" : get_d7_sign(longitude)}
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
def get_d10_sign(longitude):
    sign_index = int(longitude // 30)
    sign = SIGNS[sign_index]
    degree_in_sign = longitude % 30
    dashamsha_number = int(degree_in_sign // 3)
    if sign in ODD_SIGNS:
        start_index = sign_index
    else:
        start_index = (sign_index + 8) % 12
    destination_index = (start_index + dashamsha_number) % 12
    return SIGNS[destination_index]
def get_d10_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d10_sign" : get_d10_sign(longitude)}
    return result
def get_d12_sign(longitude):
    sign_index = int(longitude // 30)
    degree_in_sign = longitude % 30
    dwadashamsha_number = int(degree_in_sign // 2.5)
    destination_index = (sign_index + dwadashamsha_number) % 12
    return SIGNS[destination_index]
def get_d12_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d12_sign" : get_d12_sign(longitude)}
    return result
def get_d16_sign(longitude):
    sign_index = int(longitude // 30)
    sign = SIGNS[sign_index]
    degree_in_sign = longitude % 30
    shodashamsha_number = int(degree_in_sign // (30 / 16))
    if sign in MOVABLE_SIGNS:
        start_index = 0
    elif sign in FIXED_SIGNS:
        start_index = 4
    else:
        start_index = 8
    destination_index = (start_index + shodashamsha_number) % 12
    return SIGNS[destination_index]
def get_d16_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d16_sign" : get_d16_sign(longitude)}
    return result
def get_d20_sign(longitude):
    sign_index = int(longitude // 30)
    sign = SIGNS[sign_index]
    degree_in_sign = longitude % 30
    vimsamsa_number = int(degree_in_sign // (30 / 20))
    if sign in MOVABLE_SIGNS:
        start_index = 0
    elif sign in FIXED_SIGNS:
        start_index = 8
    else:
        start_index = 4
    destination_index = (start_index + vimsamsa_number) % 12
    return SIGNS[destination_index]
def get_d20_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d20_sign" : get_d20_sign(longitude)}
    return result
def get_d24_sign(longitude):
    sign_index = int(longitude // 30)
    degree_in_sign = longitude % 30
    siddhamsa_number = int(degree_in_sign // (30 / 24))
    if sign_index % 2 == 0:
        start_index = 4
    else:
        start_index = 3
    destination_index = (start_index + siddhamsa_number) % 12
    return SIGNS[destination_index]
def get_d24_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d24_sign" : get_d24_sign(longitude)}
    return result
def get_d27_sign(longitude):
    sign_index = int(longitude // 30)
    sign = SIGNS[sign_index]
    degree_in_sign = longitude % 30
    bhamsha_number = int(degree_in_sign // (30 / 27))
    if sign in FIRE_SIGNS:
        start_index = 0
    elif sign in EARTH_SIGNS:
        start_index = 3
    elif sign in AIR_SIGNS:
        start_index = 6
    else:
        start_index = 9
    destination_index = (start_index + bhamsha_number) % 12
    print({"sign" : sign, "start_index" : start_index, "destination_index" : destination_index, "result" : SIGNS[destination_index]})
    return SIGNS[destination_index]
def get_d27_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d27_sign" : get_d27_sign(longitude)}
    return result
def get_d30_sign(longitude):
    pass
def get_d30_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d30_sign" : get_d30_sign(longitude)}
    return result
def get_d40_sign(longitude):
    pass
def get_d40_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d40_sign" : get_d40_sign(longitude)}
    return result
def get_d45_sign(longitude):
    pass
def get_d45_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d45_sign" : get_d45_sign(longitude)}
    return result
def get_d60_sign(longitude):
    pass
def get_d60_chart(planets):
    result = {}
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        result[planet_name] = {"d60_sign" : get_d60_sign(longitude)}
    return result
print(get_d27_sign(74.53))