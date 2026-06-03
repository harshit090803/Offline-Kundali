from app.database.db import engine
from app.models.base import Base
from app.models.city import City
Base.metadata.create_all(bind = engine)
