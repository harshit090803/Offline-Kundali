from pydantic import BaseModel
class ChartRequest(BaseModel):
    birth_date : str
    birth_time : str
    city_id : int