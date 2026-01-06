from models.vehicle import Vehicle, ElectricCar, ElectricScooter


class FleetService:
    def __init__(self):
        self.hubs = {}

    # Add Hub
    def add_hub(self, hub_name):
        if hub_name in self.hubs:
            print(f"Hub '{hub_name}' already exists.")
        else:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' created successfully.")

    #  Add Vehicle
    def add_vehicle_to_hub(self, hub_name, vehicle: Vehicle):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist. Please create it first.")
            return

        duplicate = [v for v in self.hubs[hub_name] if v == vehicle]

        if duplicate:
            print(f" Vehicle with ID '{vehicle.vehicle_id}' already exists in hub '{hub_name}'.")
            return

        self.hubs[hub_name].append(vehicle)
        print(f" Vehicle added successfully to hub '{hub_name}'.")

    #  View Hubs
    def view_all_hubs(self):
        if not self.hubs:
            print("No hubs available.")
            return

        print("\n====== Fleet Hubs ======")
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            if not vehicles:
                print("  No vehicles in this hub.")
            else:
                for v in vehicles:
                    print(" ", v)

    #  Search by Hub
    def search_by_hub(self, hub_name):
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist.")
            return

        vehicles = self.hubs[hub_name]

        if not vehicles:
            print(f"No vehicles found in hub '{hub_name}'.")
            return

        print(f"\nVehicles in Hub: {hub_name}")
        for v in vehicles:
            print(" ", v)

    #  Search by Battery
    def search_by_battery(self):
        print("\nVehicles with battery > 80%")
        found = False

        for hub, vehicles in self.hubs.items():
            high_battery = list(filter(lambda v: v.get_battery_percentage() > 80, vehicles))

            if high_battery:
                found = True
                print(f"\nHub: {hub}")
                for v in high_battery:
                    print(" ", v)

        if not found:
            print("No vehicles found with battery > 80%.")
