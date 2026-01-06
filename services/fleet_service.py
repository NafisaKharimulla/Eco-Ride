from models.vehicle import Vehicle

class FleetService:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        for v in self.vehicles:
            if v.vehicle_id == vehicle.vehicle_id:
                raise ValueError(f"Vehicle with ID {vehicle.vehicle_id} already exists!")
        self.vehicles.append(vehicle)
        return vehicle

    def get_all_vehicles(self):
        return self.vehicles

    # Update maintenance or rental price by vehicle ID
    def update_maintenance(self, vehicle_id: str, status: str):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                v.set_maintenance_status(status)
                return v
        raise ValueError(f"Vehicle with ID {vehicle_id} not found.")

    def update_rental_price(self, vehicle_id: str, price: float):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                v.set_rental_price(price)
                return v
        raise ValueError(f"Vehicle with ID {vehicle_id} not found.")
