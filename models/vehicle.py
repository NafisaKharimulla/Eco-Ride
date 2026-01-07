class Vehicle:
    def __init__(self, vehicle_id, model, battery_level, status="Available"):
        self.vehicle_id = vehicle_id
        self.model = model

        if battery_level < 0 or battery_level > 100:
            raise ValueError("Battery level must be between 0–100")
        self.battery_level = battery_level

        self.__maintenance_status = "Good"
        self.__status = status

    #  Encapsulation Getters / Setters
    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        allowed = ["Available", "On Trip", "Under Maintenance"]
        if new_status not in allowed:
            raise ValueError("Invalid status")
        self.__status = new_status

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, new_status):
        self.__maintenance_status = new_status

    # Polymorphism (base)
    def calculate_trip_cost(self):
        return 0

    #  Data Integrity (Duplicate Check)
    def __eq__(self, other):
        return isinstance(other, Vehicle) and self.vehicle_id == other.vehicle_id

    def __str__(self):
        return (f"ID: {self.vehicle_id}, Model: {self.model}, "
                f"Battery: {self.battery_level}%, "
                f"Status: {self.__status}")
