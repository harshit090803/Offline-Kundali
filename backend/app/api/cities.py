from fastapi import APIRouter
from app.database.db import SessionLocal
from app.models.city import City
router = APIRouter()
@router.get("/cities")
def get_cities():
    db = SessionLocal()
    cities = db.query(City).all()
    result = []
    for city in cities:
        result.append({
            "city" : city.city,
            "state" : city.state,
            "country" : city.country
        })
    return result