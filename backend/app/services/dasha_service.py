from app.services.constants import (NAKSHATRAS, NAKSHATRA_LORDS)
from app.services.constants import (DASHA_YEARS, NAKSHATRA_LORDS)
from datetime import datetime, timedelta
from app.services.constants import (DASHA_SEQUENCE, DASHA_YEARS)
def get_birth_dasha(moon_longitude):
    nak_length = 360 / 27
    nak_index = int(moon_longitude // nak_length)
    nakshatra = NAKSHATRAS[nak_index]
    lord = NAKSHATRA_LORDS[nak_index]
    return {"nakshatra": nakshatra, "lord": lord}
def get_dasha_balance(moon_longitude):
    nak_length = 360 / 27
    nak_index = int(moon_longitude // nak_length)
    lord = NAKSHATRA_LORDS[nak_index]
    years = DASHA_YEARS[lord]
    start_degree = (nak_index * nak_length)
    travelled = (moon_longitude - start_degree)
    remaining_fraction = (nak_length - travelled) / nak_length
    balance_years = (years * remaining_fraction)
    return {"mahadasha" : lord, "balance_years" : round(balance_years, 2)}
def get_current_mahadasha(birth_date, birth_mahadasha, balance_years):
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    current_start = birth
    current_end = birth + timedelta(days=balance_years * 365.25)
    current_index = (DASHA_SEQUENCE.index(birth_mahadasha))
    today = datetime.now()
    if birth <= today <= current_end:
        return {"mahadasha": birth_mahadasha, "start": current_start.date(), "end": current_end.date()}
    current_start = current_end
    while True:
        current_index = (current_index + 1) % len(DASHA_SEQUENCE)
        md = DASHA_SEQUENCE[current_index]
        years = DASHA_YEARS[md]
        current_end = (current_start + timedelta(days=years * 365.25))
        if (current_start <= today <= current_end):
            return {"mahadasha": md, "start": current_start.date(), "end": current_end.date()}
        current_start = current_end