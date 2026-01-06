class Vehicle:
    def __init__(self, vehicle_id, model, battery_level):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_level = battery_level

    def __str__(self):
        return f"ID: {self.vehicle_id}, Model: {self.model}, Battery: {self.battery_level}%"
