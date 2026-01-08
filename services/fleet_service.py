from models.electric_vehicle import ElectricCar, ElectricScooter
import csv
import json

class FleetService:
    def __init__(self):
        self.hubs = {}   # { hub_name : [Vehicle Objects] }

    #  UC6: Add Hub
    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' created successfully.")
        else:
            print("Hub already exists!")

    # UC7: Prevent Duplicate Vehicle IDs
    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            print("Hub does not exist. Create hub first.")
            return

        if any(v == vehicle for v in self.hubs[hub_name]):
            print("Duplicate Vehicle ID! Not allowed.")
            return

        self.hubs[hub_name].append(vehicle)
        print("Vehicle added successfully.")

    #  UC6 View
    def view_all_hubs(self):
        if not self.hubs:
            print("No hubs found.")
            return

        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            for v in vehicles:
                print(f"  {v}")

    #  UC8 Search
    def search_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])

    def search_battery_above_80(self):
        return [
            v
            for vehicles in self.hubs.values()
            for v in vehicles
            if v.battery_level > 80
        ]

    #  UC9 Categorized View
    def categorized_view(self):
        categorized = {"Car": [], "Scooter": []}

        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    categorized["Car"].append(v)
                elif isinstance(v, ElectricScooter):
                    categorized["Scooter"].append(v)

        return categorized

    #  UC10 Fleet Analytics (Status Summary)
    def get_status_summary(self):
        summary = {"Available": 0, "On Trip": 0, "Under Maintenance": 0}

        for vehicles in self.hubs.values():
            for v in vehicles:
                status = v.get_status()
                if status in summary:
                    summary[status] += 1

        return summary

    #  UC11 Sort Vehicles Alphabetically
    def sort_vehicles_in_hub(self, hub_name):
        if hub_name not in self.hubs:
            print("Hub does not exist.")
            return

        self.hubs[hub_name] = sorted(
            self.hubs[hub_name],
            key=lambda v: v.model.lower()
        )
        print(f"Vehicles in hub '{hub_name}' sorted alphabetically by model.")

    #  UC12 Advanced Sorting
    def sort_vehicles_by_battery(self, hub_name):
        if hub_name not in self.hubs:
            print("Hub does not exist.")
            return

        self.hubs[hub_name] = sorted(
            self.hubs[hub_name],
            key=lambda v: v.battery_level,
            reverse=True
        )
        print(f"Vehicles in hub '{hub_name}' sorted by battery level (high to low).")

    def sort_vehicles_by_fare(self, hub_name):
        if hub_name not in self.hubs:
            print("Hub does not exist.")
            return

        def fare_key(v):
            if isinstance(v, ElectricCar):
                return v.calculate_trip_cost(1)
            elif isinstance(v, ElectricScooter):
                return v.calculate_trip_cost(1)
            return 0

        self.hubs[hub_name] = sorted(
            self.hubs[hub_name],
            key=fare_key,
            reverse=True
        )
        print(f"Vehicles in hub '{hub_name}' sorted by fare (high to low).")

    #  UC13 CSV File I/O
    def save_to_csv(self, filename="fleet_data.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "hub_name", "vehicle_type", "vehicle_id", "model",
                "battery_level", "status", "seating_capacity", "max_speed_limit"
            ])
            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    vehicle_type = "Car" if isinstance(v, ElectricCar) else "Scooter"
                    seats = v.seating_capacity if isinstance(v, ElectricCar) else ""
                    speed = v.max_speed_limit if isinstance(v, ElectricScooter) else ""
                    writer.writerow([
                        hub, vehicle_type, v.vehicle_id, v.model,
                        v.battery_level, v.get_status(), seats, speed
                    ])
        print(f"Fleet saved to '{filename}' successfully.")

    def load_from_csv(self, filename="fleet_data.csv"):
        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    hub = row["hub_name"]
                    vtype = row["vehicle_type"]
                    vid = row["vehicle_id"]
                    model = row["model"]
                    battery = int(row["battery_level"])
                    status = row["status"]

                    if hub not in self.hubs:
                        self.hubs[hub] = []

                    if vtype == "Car":
                        seats = int(row["seating_capacity"])
                        vehicle = ElectricCar(vid, model, battery, status, seats)
                    elif vtype == "Scooter":
                        speed = int(row["max_speed_limit"])
                        vehicle = ElectricScooter(vid, model, battery, status, speed)
                    else:
                        continue

                    if not any(v == vehicle for v in self.hubs[hub]):
                        self.hubs[hub].append(vehicle)
            print(f"Fleet loaded from '{filename}' successfully.")
        except FileNotFoundError:
            print(f"No existing CSV fleet data found. Starting fresh.")

    #  UC14 JSON File I/O
    def save_to_json(self, filename="fleet_data.json"):
        data = {}
        for hub, vehicles in self.hubs.items():
            data[hub] = []
            for v in vehicles:
                vehicle_dict = {
                    "vehicle_type": "Car" if isinstance(v, ElectricCar) else "Scooter",
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery_level": v.battery_level,
                    "status": v.get_status(),
                }
                if isinstance(v, ElectricCar):
                    vehicle_dict["seating_capacity"] = v.seating_capacity
                elif isinstance(v, ElectricScooter):
                    vehicle_dict["max_speed_limit"] = v.max_speed_limit
                data[hub].append(vehicle_dict)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Fleet saved to '{filename}' successfully.")

    def load_from_json(self, filename="fleet_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for hub, vehicles in data.items():
                    if hub not in self.hubs:
                        self.hubs[hub] = []
                    for v in vehicles:
                        vtype = v.get("vehicle_type")
                        vid = v.get("vehicle_id")
                        model = v.get("model")
                        battery = int(v.get("battery_level"))
                        status = v.get("status")

                        if vtype == "Car":
                            seats = int(v.get("seating_capacity", 4))
                            vehicle = ElectricCar(vid, model, battery, status, seats)
                        elif vtype == "Scooter":
                            speed = int(v.get("max_speed_limit", 60))
                            vehicle = ElectricScooter(vid, model, battery, status, speed)
                        else:
                            continue

                        if not any(existing_v == vehicle for existing_v in self.hubs[hub]):
                            self.hubs[hub].append(vehicle)
            print(f"Fleet loaded from '{filename}' successfully.")
        except FileNotFoundError:
            print(f"No JSON file found. Starting fresh.")
