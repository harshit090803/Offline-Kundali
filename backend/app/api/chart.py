from fastapi import APIRouter

from app.services.planet_service import (
    get_all_planets
)

router = APIRouter()


@router.get("/chart/planets")
def planets():

    result = get_all_planets(
        birth_date="2003-08-10",
        birth_time="14:30"
    )

    return result