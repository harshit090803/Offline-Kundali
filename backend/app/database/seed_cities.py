from app.database.db import SessionLocal
from app.models.city import City
db = SessionLocal()
cities = [City(city = "Kanpur", state = "Uttar Pradesh",  country = "India",  latitude = "26.4499", longitude = "80.3319", timezone = "Asia/Kolkata"), City(city = "Delhi", state = "Delhi", country = "India", latitude = "28.6139", longitude = "77.2090", timezone = "Asia/Kolkata"), City(city = "Mumbai", state = "Maharashtra", country = "India", latitude = "19.0760", longitude = "72.8777", timezone = "Asia/Kolkata")]
db.add_all(cities)
db.commit()
print("Cities Inserted")