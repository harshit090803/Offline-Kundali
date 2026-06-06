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
def get_dignity(planet, sign):
    if planet in EXALTATION_SIGNS:
        if sign == EXALTATION_SIGNS[planet]:
            return "Exalted"
    if planet in DEBILITATION_SIGNS:
        if sign == DEBILITATION_SIGNS[planet]:
            return "Debilitated"
    if planet in OWN_SIGNS:
        if sign in OWN_SIGNS[planet]:
            return "Own Sign"
    return "Normal"
