from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float, seating_capacity: int):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def __str__(self):
        return (
            super().__str__() +
            f", Seating Capacity: {self.seating_capacity}"
        )

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float, max_speed_limit: float):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def __str__(self):
        return (
            super().__str__() +
            f", Max Speed Limit: {self.max_speed_limit} km/h"
        )
