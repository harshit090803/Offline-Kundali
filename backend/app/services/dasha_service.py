from re import A
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
def get_antardasha_periods(mahadasha):
    md_years = DASHA_YEARS[mahadasha]
    periods = []
    for ad in DASHA_SEQUENCE:
        ad_years = (md_years  * DASHA_YEARS[ad]) / 120
        periods.append({"antardasha" : ad, "years" : round(ad_years, 2)})
    return periods
def get_current_antardasha(mahadasha, md_start_date):
    periods = get_antardasha_periods(mahadasha)
    current_start = md_start_date
    today = datetime.now()
    for period in periods:
        current_end = (current_start + timedelta(days = period["years"] * 365.25))
        if(current_start <= today <= current_end):
            return{"mahadasha" : mahadasha, "antardasha" : period["antardasha"], "start" : current_start.date(), "end" : current_end.date()}
        current_start = (current_end)
    return None
def get_birth_mahadasha_data(moon_longitude):
    balance = get_dasha_balance(moon_longitude)
    return{"birth_mahadasha" : balance["mahadasha"], "birth_balance" : balance["balance_years"]}
def get_complete_dasha(birth_date, moon_longitude):
    birth_data = (get_birth_mahadasha_data(moon_longitude))
    current_md = (get_current_mahadasha(birth_date, birth_data["birth_mahadasha"], birth_data["birth_balance"]))
    md_start = datetime.combine(current_md["start"], datetime.min.time())
    current_ad = (get_current_antardasha(current_md["mahadasha"], md_start))
    return {"birth_mahadasha" : birth_data["birth_mahadasha"], "birth_balance" : birth_data["birth_balance"], "current_mahadasha" : current_md["mahadasha"], "current_antardasha" : current_ad["antardasha"], "md_start" : current_md["start"], "md_end" : current_md["end"], "ad_start" : current_ad["start"], "ad_end" : current_ad["end"]}
def get_pratyantar_periods(mahadasha, antardasha):
    md_years = DASHA_YEARS[mahadasha]
    ad_years = (md_years * DASHA_YEARS[antardasha]) / 120
    periods = []
    for pd in DASHA_SEQUENCE:
        pd_years = (ad_years * DASHA_YEARS[pd]) / 120
        periods.append({"pratyantar" : pd, "years" : round(pd_years, 4)})
    return periods
def get_current_pratyantar(mahadasha, antardasha, ad_start_date):
    periods = get_pratyantar_periods(mahadasha, antardasha)
    current_start = (ad_start_date)
    today = datetime.now()
    for period in periods:
        current_end = (current_start + timedelta(days= period["years"] * 365.25))
        if (current_start <= today <= current_end):
            return {"pratyantar": period["pratyantar"], "start": current_start.date(), "end": current_end.date()}
        current_start = (current_end)
    return None
def get_complete_dasha(birth_date, moon_longitude):
    birth_data = (get_birth_mahadasha_data(moon_longitude))
    current_md = (get_current_mahadasha(birth_date, birth_data["birth_mahadasha"], birth_data["birth_balance"]))
    md_start = datetime.combine(current_md["start"], datetime.min.time())
    current_ad = (get_current_antardasha(current_md["mahadasha"], md_start))
    ad_start = datetime.combine(current_ad["start"], datetime.min.time())
    current_pd = (get_current_pratyantar(current_md["mahadasha"], current_ad["antardasha"], ad_start))
    pd_start = datetime.combine(current_pd["start"], datetime.min.time())
    current_sd = (get_current_sookshma(current_md["mahadasha"], current_ad["antardasha"], current_pd["pratyantar"], pd_start))
    return {"birth_mahadasha": birth_data["birth_mahadasha"], "birth_balance": birth_data["birth_balance"], "current_mahadasha": current_md["mahadasha"], "current_antardasha" : current_ad["antardasha"], "current_pratyantar": current_pd["pratyantar"], "md_start": current_md["start"], "md_end": current_md["end"], "ad_start": current_ad["start"], "ad_end": current_ad["end"], "pd_start": current_pd["start"],  "pd_end": current_pd["end"], "sd_start": current_sd["start"], "sd_end": current_sd["end"]}
def get_sookshma_periods(mahadasha, antardasha, pratyantar):
    md_years = DASHA_YEARS[mahadasha]
    ad_years = (md_years * DASHA_YEARS[antardasha]) / 120
    pd_years = (ad_years * DASHA_YEARS[pratyantar]) / 120
    periods = []
    for sd in DASHA_SEQUENCE:
        sd_years = (pd_years * DASHA_YEARS[sd]) / 120
        periods.append({"sookshma": sd, "years": round(sd_years, 6)})
    return periods
def get_current_sookshma(mahadasha, antardasha, pratyantar, pd_start_date):
    periods = get_sookshma_periods(mahadasha, antardasha, pratyantar)
    current_start = pd_start_date
    today = datetime.now()
    for period in periods:
        current_end = (current_start + timedelta(days=period["years"] * 365.25))
        if current_start <= today <= current_end:
            return {"sookshma": period["sookshma"], "start": current_start.date(), "end": current_end.date()}
        current_start = current_end
    return None