EXALTATION_SIGNS = {
    "Sun": "Aries",
    "Moon": "Taurus",
    "Mars": "Capricorn",
    "Mercury": "Virgo",
    "Jupiter": "Cancer",
    "Venus": "Pisces",
    "Saturn": "Libra",
    "Rahu" : "Taurus",
    "Ketu" : "Scorpio"
}
DEBILITATION_SIGNS = {
    "Sun": "Libra",
    "Moon": "Scorpio",
    "Mars": "Cancer",
    "Mercury": "Pisces",
    "Jupiter": "Capricorn",
    "Venus": "Virgo",
    "Saturn": "Aries",
    "Rahu" : "Scorpio",
    "Ketu" : "Taurus"
}
OWN_SIGNS = {

    "Sun": ["Leo"],

    "Moon": ["Cancer"],

    "Mars": ["Aries", "Scorpio"],

    "Mercury": ["Gemini", "Virgo"],

    "Jupiter": ["Sagittarius", "Pisces"],

    "Venus": ["Taurus", "Libra"],

    "Saturn": ["Capricorn", "Aquarius"]

}
COMBUSTION_LIMITS = {

    "Moon": 12,

    "Mars": 17,

    "Mercury": 14,

    "Jupiter": 11,

    "Venus": 10,

    "Saturn": 15

}
MOOLTRIKONA_SIGNS = {

    "Sun": "Leo",

    "Moon": "Taurus",

    "Mars": "Aries",

    "Mercury": "Virgo",

    "Jupiter": "Sagittarius",

    "Venus": "Libra",

    "Saturn": "Aquarius"

}
MOOLTRIKONA_RANGES = {

    "Sun": ("Leo", 0, 20),

    "Moon": ("Taurus", 4, 30),

    "Mars": ("Aries", 0, 12),

    "Mercury": ("Virgo", 16, 20),

    "Jupiter": ("Sagittarius", 0, 10),

    "Venus": ("Libra", 0, 15),

    "Saturn": ("Aquarius", 0, 20)

}
PLANET_RELATIONS = {

    "Sun": {
        "friend": ["Moon", "Mars", "Jupiter"],
        "enemy": ["Venus", "Saturn"],
        "neutral": ["Mercury"]
    },

    "Moon": {
        "friend": ["Sun", "Mercury"],
        "enemy": [],
        "neutral": ["Mars", "Jupiter", "Venus", "Saturn"]
    },

    "Mars": {
        "friend": ["Sun", "Moon", "Jupiter"],
        "enemy": ["Mercury"],
        "neutral": ["Venus", "Saturn"]
    },

    "Mercury": {
        "friend": ["Sun", "Venus"],
        "enemy": ["Moon"],
        "neutral": ["Mars", "Jupiter", "Saturn"]
    },

    "Jupiter": {
        "friend": ["Sun", "Moon", "Mars"],
        "enemy": ["Mercury", "Venus"],
        "neutral": ["Saturn"]
    },

    "Venus": {
        "friend": ["Mercury", "Saturn"],
        "enemy": ["Sun", "Moon"],
        "neutral": ["Mars", "Jupiter"]
    },

    "Saturn": {
        "friend": ["Mercury", "Venus"],
        "enemy": ["Sun", "Moon"],
        "neutral": ["Mars", "Jupiter"]
    }

}
SIGN_LORDS = {

    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter"

}
def get_dignity(planet, sign, longitude):
    if planet in EXALTATION_SIGNS:
        if sign == EXALTATION_SIGNS[planet]:
            return "Exalted"
    if planet in DEBILITATION_SIGNS:
        if sign == DEBILITATION_SIGNS[planet]:
            return "Debilitated"
    if is_mooltrikona(planet, sign, longitude):
        return "Mooltrikona"
    if planet in OWN_SIGNS:
        if sign in OWN_SIGNS[planet]:
            return "Own Sign"
    return get_sign_relationship(planet, sign)
def is_combust(planet, planet_longitude, sun_longitude):
    if planet not in COMBUSTION_LIMITS:
        return False
    difference = abs(planet_longitude - sun_longitude)
    if difference > 180:
        difference = (360 - difference)
    return (difference <= COMBUSTION_LIMITS[planet])
def is_mooltrikona( planet, sign, longitude):
    if planet not in MOOLTRIKONA_RANGES:
        return False
    m_sign, start_deg, end_deg = (MOOLTRIKONA_RANGES[planet])
    if sign != m_sign:
        return False
    degree_in_sign = (longitude % 30)
    return (start_deg <= degree_in_sign < end_deg)
def get_sign_relationship(planet, sign):
    if planet not in PLANET_RELATIONS:
        return "Normal"
    sign_lord = SIGN_LORDS[sign]
    relations = PLANET_RELATIONS[planet]
    if sign_lord in relations["friend"]:
        return "Friendly Sign"
    if sign_lord in relations["enemy"]:
        return "Enemy Sign"
    return "Neutral Sign"