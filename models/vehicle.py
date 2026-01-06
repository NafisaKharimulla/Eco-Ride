from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = None
        self.set_battery_percentage(battery_percentage)

    @abstractmethod
    def calculate_trip_cost(self, value):
        """Implemented differently in each child class"""
        pass

    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, value: float):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100.")

    def __str__(self):
        return f"{self.vehicle_id} - {self.model} ({self.__battery_percentage}%)"
