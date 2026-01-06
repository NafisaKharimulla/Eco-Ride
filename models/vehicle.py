from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = battery_percentage

        # Encapsulation
        self.__maintenance_status = "Good"
        self.__rental_price = 0

    #  Getters
    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price

    #  Setters
    def set_battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Price cannot be negative")

    # Equality Check
    def __eq__(self, other):
        return isinstance(other, Vehicle) and self.vehicle_id == other.vehicle_id

    # Mandatory Method
    @abstractmethod
    def calculate_trip_cost(self, value):
        pass

    def __str__(self):
        return f"[{self.vehicle_id}] {self.model} | Battery: {self.__battery_percentage}%"


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5 + (0.5 * distance)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed = max_speed

    def calculate_trip_cost(self, minutes):
        return 1 + (0.15 * minutes)
