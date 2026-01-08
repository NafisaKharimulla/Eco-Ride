from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_level, status="Available", seating_capacity=4):
        super().__init__(vehicle_id, model, battery_level, status)
        self.seating_capacity = seating_capacity

    # UC5 Polymorphism
    def calculate_trip_cost(self, distance_km):
        return 5.0 + (0.5 * distance_km)

    def __str__(self):
        return f"[Car] {super().__str__()}, Seats: {self.seating_capacity}"

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_level, status="Available", max_speed_limit=60):
        super().__init__(vehicle_id, model, battery_level, status)
        self.max_speed_limit = max_speed_limit

    # UC5 Polymorphism
    def calculate_trip_cost(self, minutes):
        return 1.0 + (0.15 * minutes)

    def __str__(self):
        return f"[Scooter] {super().__str__()}, Max Speed: {self.max_speed_limit} km/h"
