from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def calculate_trip_cost(self, distance_km):
        return 5.0 + (0.5 * distance_km)

    def __str__(self):
        return f"[Car] {super().__str__()}"


class ElectricScooter(Vehicle):
    def calculate_trip_cost(self, minutes):
        return 1.0 + (0.15 * minutes)

    def __str__(self):
        return f"[Scooter] {super().__str__()}"
