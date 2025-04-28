import datetime

import faust


class Solar(faust.Record, serializer="json"):
    date: datetime.date
    solar_mwh: float
    solar_capacity: float
    year: int
