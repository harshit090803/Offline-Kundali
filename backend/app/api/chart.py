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
router = APIRouter()
@router.post("/chart/generate")
def generate_chart(request : ChartRequest):
    city = get_city(request.city_id)
    ascendant = get_ascendant(request.birth_date, request.birth_time, float(city.latitude), float(city.longitude))
    houses = get_houses(request.birth_date, request.birth_time, float(city.latitude), float(city.longitude))    
    planets = get_all_planets(request.birth_date, request.birth_time)
    for planet_name in planets:
        longitude = planets[planet_name]["longitude"]
        planets[planet_name]["house"] = find_house(longitude,houses)
    return {"city" : city.city, "state" : city.state, "country" : city.country, "ascendant" : ascendant, "planets" : planets}
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