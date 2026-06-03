import swisseph as swe
class D1Generator:
    def __init__(self):
        swe.set_ephe_path(".")
    def test(self):
        return "Swiss Ephemeris Connected"