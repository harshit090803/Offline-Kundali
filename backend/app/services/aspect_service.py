def angular_distance(longitude1, longitude2):
    difference = abs(longitude1 - longitude2)
    if difference > 180:
        difference = (360 - difference)
    return difference
def has_seventh_aspect(longitude1, longitude2):
    distance = angular_distance(longitude1, longitude2)
    return (abs(distance - 180) <= 5)
def has_aspect(longitude1, longitude2, target_angle):
    distance = (longitude2 - longitude1) % 360
    return (abs(distance - target_angle) <= 8)
def get_aspects(planets):
    aspects = []
    planet_names = list(planets.keys())
    for p1 in planet_names:
        for p2 in planet_names:
            if p1 == p2:
                continue
            lon1 = planets[p1]["longitude"]
            lon2 = planets[p2]["longitude"]
            if has_seventh_aspect(lon1, lon2):
                aspects.append({"from": p1, "to": p2, "type": "7th Aspect"})
            if p1 == "Mars":
                if has_aspect(lon1, lon2, 90):
                    aspects.append({"from": p1, "to": p2, "type": "4th Aspect"})
                if has_aspect(lon1, lon2, 210):
                    aspects.append({"from": p1, "to": p2, "type": "8th Aspect"})
            if p1 == "Jupiter":
                if has_aspect(lon1, lon2, 120):
                    aspects.append({"from": p1, "to": p2, "type": "5th Aspect"})
                if has_aspect(lon1, lon2, 240):
                    aspects.append({"from": p1, "to": p2, "type": "9th Aspect"})
            if p1 == "Saturn":
                if has_aspect(lon1, lon2, 60):
                    aspects.append({"from": p1, "to": p2, "type": "3rd Aspect"})
                if has_aspect(lon1, lon2, 270):
                    aspects.append({"from": p1, "to": p2, "type": "10th Aspect"})
    return aspects