from services.fleet_service import FleetService
from models.electric_vehicle import ElectricCar, ElectricScooter

def main():

    print("Welcome to Eco-Ride Urban Mobility System")

    fleet = FleetService()

    while True:
        print("\n=== Eco Ride Fleet System ===")
        print("1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Search Vehicles in Hub")
        print("5. Search Vehicles Battery > 80%")
        print("6. Categorized View (Cars / Scooters)")
        print("7. Fleet Analytics (Status Summary)")
        print("8. Exit")

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
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
