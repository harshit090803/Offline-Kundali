def find_house(planet_longitude, house_cusps):
    cusps = list(house_cusps.values())
    for i in range(12):
        current_house = cusps[i]
        next_house = cusps[(i + 1) % 12]
        if next_house < current_house:
            next_house += 360
        test_longitude = (planet_longitude)
        if (test_longitude < current_house):
            test_longitude += 360
        if (current_house <= test_longitude < next_house):
            return i + 1
    return 12