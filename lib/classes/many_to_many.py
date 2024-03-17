def is_valid_name(name):
    return isinstance(name, str) and 1 <= len(name) <= 15

def is_valid_date(date):
    # Assuming date is valid if it's a string with at least 7 characters
    return isinstance(date, str) and len(date) >= 7

class Visitor:
    def __init__(self, name):
        if not is_valid_name(name):
            raise ValueError("Invalid name")
        self.name = name
        self.trips = []

    def add_trip(self, trip):
        if not isinstance(trip, Trip):
            raise ValueError("Invalid trip")
        self.trips.append(trip)

    def remove_trip(self, trip):
        if trip not in self.trips:
            raise ValueError("Trip not found")
        self.trips.remove(trip)

    def __str__(self):
        return f"Visitor: {self.name}, Trips: {[str(trip) for trip in self.trips]}"

class Trip:
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise ValueError("Invalid visitor")
        if not isinstance(national_park, NationalPark):
            raise ValueError("Invalid national park")
        if not is_valid_date(start_date):
            raise ValueError("Invalid start date")
        if not is_valid_date(end_date):
            raise ValueError("Invalid end date")
        if start_date > end_date:
            raise ValueError("Start date cannot be later than end date")
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Trip: {self.visitor.name} visited {self.national_park.name} from {self.start_date} to {self.end_date}"

class NationalPark:
    def __init__(self, name):
        if not is_valid_name(name):
            raise ValueError("Invalid name")
        self.name = name
        self.visitors = []

    def add_visitor(self, visitor):
        if not isinstance(visitor, Visitor):
            raise ValueError("Invalid visitor")
        self.visitors.append(visitor)

    def __str__(self):
        return f"National Park: {self.name}"

   