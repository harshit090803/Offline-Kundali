from datetime import datetime
import pytz
def local_to_utc(birth_date, birth_time, timezone_name):
    local_timezone = pytz.timezone(timezone_name)
    local_dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    local_dt = (local_timezone.localize(local_dt))
    utc_dt = (local_dt.astimezone(pytz.utc))
    return utc_dt