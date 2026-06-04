from app.database.db import SessionLocal
from app.models.city import City
def get_city(city_id):
    db = SessionLocal()
    city = (
        db.query(City)
        .filter(City.id == city_id)
        .first()
    )
    return city