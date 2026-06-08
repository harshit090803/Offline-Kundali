from fastapi import APIRouter
from app.services.ascendant_service import get_ascendant
from app.services.ascendant_service import get_houses
from app.services.planet_service import (get_all_planets)
from app.schemas.chart_schema import ChartRequest
from app.services.city_service import get_city
from app.services.chart_service import find_house
from app.services.dasha_service import (get_birth_dasha)
from app.services.dasha_service import (get_dasha_balance, get_current_mahadasha, get_antardasha_periods, get_current_antardasha, get_complete_dasha, get_pratyantar_periods)
from datetime import datetime
from app.services.time_service import (local_to_utc)
from app.services.aspect_service import get_aspects
from app.services.divisional_service import (get_d2_chart, get_d3_chart, get_d4_chart, get_d7_chart, get_d9_chart, get_d10_chart, get_d12_chart, get_d16_chart, get_d20_chart, get_d24_chart, get_d27_chart, get_d30_chart, get_d40_chart, get_d45_chart, get_d60_chart, get_d27_sign)
from app.services.constants import (SIGNS, FIRE_SIGNS, EARTH_SIGNS, AIR_SIGNS, WATER_SIGNS)
router = APIRouter()
@router.post("/chart/generate")
def generate_chart(request : ChartRequest):
    city = get_city(request.city_id)
    ascendant = get_ascendant(request.birth_date, request.birth_time, float(city.latitude), float(city.longitude))
    houses = get_houses(request.birth_date, request.birth_time, float(city.latitude), float(city.longitude))    
    planets = get_all_planets(request.birth_date, request.birth_time)
    aspects = get_aspects(planets)
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        planets[planet_name]["house"] = find_house(longitude,houses)
    return {"city" : city.city, "state" : city.state, "country" : city.country, "ascendant" : ascendant, "planets" : planets, "aspects" : aspects}
@router.get("/chart/planets")
def planets():
    result = get_all_planets(birth_date="2003-08-10", birth_time="14:30")
    return result
@router.post("/chart/houses")
def houses(request: ChartRequest):
    city = get_city(request.city_id)
    return get_houses(request.birth_date, request.birth_time, float(city.latitude), float(city.longitude))
@router.get("/chart/dasha-test")
def dasha_test():
    planets = get_all_planets("2003-08-10","14:30")
    moon_longitude = planets["Moon"]["longitude"]
    return get_birth_dasha(moon_longitude)
@router.get("/chart/dasha-balance")
def dasha_balance():
    planets = get_all_planets("2003-08-10", "14:30")
    moon_longitude = planets["Moon"]["longitude"]
    return get_dasha_balance(moon_longitude)
@router.get("/chart/current-mahadasha")
def current_mahadasha():
    planets = get_all_planets("2003-08-10", "14:30")
    moon_longitude = planets["Moon"]["longitude"]
    balance = get_dasha_balance(moon_longitude)
    return get_current_mahadasha("2003-08-10", balance["mahadasha"], balance["balance_years"])
@router.get("/chart/antardasha-test")
def antardasha_test():
    return get_antardasha_periods("Rahu")
@router.get("/chart/current-antardasha")
def current_antardasha():
    md = get_current_mahadasha("2003-08-10", "Mars", 3.87)
    start_date = datetime.combine(md["start"], datetime.min.time())
    return get_current_antardasha(md["mahadasha"], start_date)
@router.post("/chart/dasha")
def dasha(request: ChartRequest):
    planets = get_all_planets(request.birth_date, request.birth_time)
    moon_longitude = planets["Moon"]["longitude"]
    return get_complete_dasha(request.birth_date, moon_longitude)
@router.get("/chart/pratyantar-test")
def pratyantar_test():
    return get_pratyantar_periods("Jupiter", "Venus")
@router.get("/chart/time-test")
def time_test():
    return str(local_to_utc("2003-08-10", "14:30", "Asia/Kolkata"))
@router.get("/chart/d2-test")
def d2_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d2_chart(planets)
@router.get("/chart/d3-test")
def d3_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d3_chart(planets)
@router.get("/chart/d4-test")
def d4_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d4_chart(planets)
@router.get("/chart/d7-test")
def d7_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d7_chart(planets)
@router.get("/chart/d9-test")
def d9_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d9_chart(planets)
@router.get("/chart/d10-test")
def d10_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d10_chart(planets)
@router.get("/chart/d12-test")
def d12_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d12_chart(planets)
@router.get("/chart/d16-test")
def d16_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d16_chart(planets)
@router.get("/chart/d20-test")
def d20_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d20_chart(planets)
@router.get("/chart/d24-test")
def d24_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d24_chart(planets)
@router.get("/chart/d27-test")
def d27_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d27_chart(planets)
@router.get("/chart/d30-test")
def d30_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d30_chart(planets)
@router.get("/chart/d40-test")
def d40_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d40_chart(planets)
@router.get("/chart/d45-test")
def d45_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d45_chart(planets)
@router.get("/chart/d60-test")
def d60_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return get_d60_chart(planets)
@router.get("/chart/rahu-test")
def rahu_test():
    planets = get_all_planets("2003-08-10", "14:30")
    return {"Rahu": planets["Rahu"], "Ketu": planets["Ketu"]}
@router.get("/chart/test")
@router.get("/chart/test")
def test():
    return get_d27_sign(74.53)
@router.get("/chart/test2")
def test2():
    return {"AIR_SIGNS": AIR_SIGNS}