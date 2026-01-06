from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float, seating_capacity: int):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance: float):
        """ElectricCar: Cost = rental price per km * distance + fixed fee"""
        return self.get_rental_price() * distance + 10  # e.g., fixed fee $10

    def __str__(self):
        return super().__str__() + f", Seating Capacity: {self.seating_capacity}"


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float, max_speed_limit: float):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance: float):
        """ElectricScooter: Cost = rental price per km * distance"""
        return self.get_rental_price() * distance

    def __str__(self):
        return super().__str__() + f", Max Speed Limit: {self.max_speed_limit} km/h"
