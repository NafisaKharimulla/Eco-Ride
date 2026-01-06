class Vehicle:
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = None
        self.__maintenance_status = "OK"   # Private attribute
        self.__rental_price = 0.0          # Private attribute

        #setter to validate battery
        self.set_battery_percentage(battery_percentage)


    # Battery Percentage Getter/Setter

    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, value: float):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100.")


    # Maintenance Status Getter/Setter

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status: str):
        if status in ["OK", "Needs Service", "Under Maintenance"]:
            self.__maintenance_status = status
        else:
            raise ValueError("Invalid maintenance status.")


    # Rental Price Getter/Setter

    def get_rental_price(self):
        return self.__rental_price

    def set_rental_price(self, price: float):
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price cannot be negative.")




    def __str__(self):
        return (
            f"Vehicle ID: {self.vehicle_id}, Model: {self.model}, "
            f"Battery: {self.__battery_percentage}%, "
            f"Maintenance Status: {self.__maintenance_status}, "
            f"Rental Price: ${self.__rental_price}"
        )
