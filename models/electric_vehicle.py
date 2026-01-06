from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance_km: float):
        return 5.0 + (0.50 * distance_km)

    def __str__(self):
        return super().__str__() + f" | Car | Seats: {self.seating_capacity}"


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, minutes: float):
        return 1.0 + (0.15 * minutes)

    def __str__(self):
        return super().__str__() + f" | Scooter | Max Speed: {self.max_speed_limit} km/h"
