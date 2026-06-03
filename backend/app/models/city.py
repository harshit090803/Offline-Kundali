from sqlalchemy import Column, Integer, String
from app.models.base import Base
class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key = True, index = True)
    city = Column(String, nullable = False)
    state = Column(String)
    country = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    timezone = Column(String)