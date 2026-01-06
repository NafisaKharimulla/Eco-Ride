from models.vehicle import Vehicle

class FleetService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def get_all_vehicles(self):
        return self.vehicles
