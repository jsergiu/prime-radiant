class BirthInfoSet:
    year: int
    month: int
    day: int
    place: str

    def __init__(self, year, month, day, place):
        self.year = year
        self.month = month
        self.day = day
        self.place = place