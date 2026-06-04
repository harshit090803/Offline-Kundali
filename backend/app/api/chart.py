from fastapi import APIRouter
from app.services.ascendant_service import get_ascendant
from app.services.ascendant_service import get_houses
from app.services.planet_service import (
    get_all_planets
)
from app.schemas.chart_schema import ChartRequest
from app.services.city_service import get_city
from app.services.chart_service import find_house
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
    return {
        "city" : city.city,
        "state" : city.state,
        "country" : city.country,
        "ascendant" : ascendant,
        "planets" : planets
    }
@router.get("/chart/planets")
def planets():
    result = get_all_planets(birth_date="2003-08-10", birth_time="14:30")
    return result
@router.post("/chart/houses")
def houses(request: ChartRequest):
    city = get_city(request.city_id)
    return get_houses(request.birth_date, request.birth_time, float(city.latitude), float(city.longitude))