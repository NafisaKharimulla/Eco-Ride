from models.electric_vehicle import ElectricCar, ElectricScooter


class FleetService:
    def __init__(self):
        self.hubs = {}  # { hub_name : [vehicles] }

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' created successfully.")
        else:
            print("Hub already exists!")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            print("Hub does not exist. Create hub first.")
            return

        if any(v == vehicle for v in self.hubs[hub_name]):
            print("Duplicate Vehicle ID! Not allowed.")
            return

        self.hubs[hub_name].append(vehicle)
        print("Vehicle added successfully.")

    def view_all_hubs(self):
        if not self.hubs:
            print("No hubs found.")
            return

        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            for v in vehicles:
                print(f"  {v}")

    def search_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])

    def search_battery_above_80(self):
        return [
            v
            for vehicles in self.hubs.values()
            for v in vehicles
            if v.battery_level > 80
        ]

    def categorized_view(self):
        categorized = {"Car": [], "Scooter": []}

        for vehicles in self.hubs.values():
            for v in vehicles:
                if "Car" in v.__class__.__name__:
                    categorized["Car"].append(v)
                else:
                    categorized["Scooter"].append(v)

        return categorized
