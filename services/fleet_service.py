from models.vehicle import Vehicle

class FleetService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        # Check for duplicate Vehicle ID
        for v in self.vehicles:
            if v.vehicle_id == vehicle.vehicle_id:
                raise ValueError(f"Vehicle with ID {vehicle.vehicle_id} already exists!")
        self.vehicles.append(vehicle)
        return vehicle

    def get_all_vehicles(self):
        return self.vehicles
