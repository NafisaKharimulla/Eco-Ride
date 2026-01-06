class FleetHubService:
    def __init__(self):
        # Key = Hub Name , Value = List of Vehicles
        self.hubs = {}

    def add_hub(self, hub_name: str):
        if hub_name in self.hubs:
            print(f"Hub '{hub_name}' already exists.")
        else:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' created successfully.")

    def add_vehicle_to_hub(self, hub_name: str, vehicle):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist.")
            return

        self.hubs[hub_name].append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to hub '{hub_name}'.")

    def get_all_hubs(self):
        return self.hubs
