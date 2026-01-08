from services.fleet_service import FleetService
from models.electric_vehicle import ElectricCar, ElectricScooter

def main():
    print("Welcome to Eco-Ride Urban Mobility System")

    fleet = FleetService()
    # Load existing data
    fleet.load_from_json()

    while True:
        print("\n=== Eco Ride Fleet System ===")
        print("1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Search Vehicles in Hub")
        print("5. Search Vehicles Battery > 80%")
        print("6. Categorized View (Cars / Scooters)")
        print("7. Fleet Analytics (Status Summary)")
        print("8. Sort Vehicles Alphabetically")
        print("9. Sort Vehicles by Battery Level")
        print("10. Sort Vehicles by Fare Price")
        print("11. Save Fleet to CSV")
        print("12. Save Fleet to JSON")
        print("13. Calculate Trip Cost")
        print("14. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            hub = input("Enter Hub Name: ")
            fleet.add_hub(hub)

        elif choice == "2":
            hub = input("Enter Hub Name: ")
            vtype = input("Enter Type (car/scooter): ").lower()
            vid = input("Enter Vehicle ID: ")
            model = input("Enter Model Name: ")
            battery = int(input("Enter Battery Level: "))
            status = input("Enter Status (Available / On Trip / Under Maintenance): ")

            if vtype == "car":
                seats = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(vid, model, battery, status, seats)
            elif vtype == "scooter":
                speed = int(input("Enter Max Speed Limit: "))
                vehicle = ElectricScooter(vid, model, battery, status, speed)
            else:
                print("Invalid type")
                continue

            fleet.add_vehicle_to_hub(hub, vehicle)

        elif choice == "3":
            fleet.view_all_hubs()

        elif choice == "4":
            hub = input("Enter Hub Name: ")
            vehicles = fleet.search_by_hub(hub)
            if vehicles:
                print(f"\nVehicles in {hub}:")
                for v in vehicles:
                    print(v)
            else:
                print("No vehicles found or hub does not exist.")

        elif choice == "5":
            results = fleet.search_battery_above_80()
            print("\nVehicles with battery > 80%:")
            for v in results:
                print(v)

        elif choice == "6":
            categorized = fleet.categorized_view()
            print("\nCars:")
            for c in categorized["Car"]:
                print(c)
            print("\nScooters:")
            for s in categorized["Scooter"]:
                print(s)

        elif choice == "7":
            summary = fleet.get_status_summary()
            print("\n===== Fleet Status Summary =====")
            print(f"Available          : {summary['Available']}")
            print(f"On Trip            : {summary['On Trip']}")
            print(f"Under Maintenance  : {summary['Under Maintenance']}")
            print("================================")

        elif choice == "8":
            hub = input("Enter Hub Name: ")
            fleet.sort_vehicles_in_hub(hub)
            fleet.view_all_hubs()

        elif choice == "9":
            hub = input("Enter Hub Name: ")
            fleet.sort_vehicles_by_battery(hub)
            fleet.view_all_hubs()

        elif choice == "10":
            hub = input("Enter Hub Name: ")
            fleet.sort_vehicles_by_fare(hub)
            fleet.view_all_hubs()

        elif choice == "11":
            fleet.save_to_csv()

        elif choice == "12":
            fleet.save_to_json()

        elif choice == "13":  # US5
            print("\n=== Calculating Trip cost ===")
            for hub, vehicles in fleet.hubs.items():
                print(f"\nHub: {hub}")
                for v in vehicles:
                    if isinstance(v, ElectricCar):
                        cost = v.calculate_trip_cost(10)  # Example km
                    elif isinstance(v, ElectricScooter):
                        cost = v.calculate_trip_cost(15)  # Example minutes
                    else:
                        cost = 0
                    print(f"{v} -> Trip Cost: ${cost:.2f}")

        elif choice == "14":
            fleet.save_to_csv()
            fleet.save_to_json()
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
