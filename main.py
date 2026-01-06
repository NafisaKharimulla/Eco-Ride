from services.fleet_service import FleetService
from models.vehicle import Vehicle


def main():
    fleet = FleetService()

    while True:
        print("\n===== Eco-Ride Multi-Hub Fleet System =====")
        print("1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Hub Name: ")
            fleet.add_hub(name)

        elif choice == "2":
            hub = input("Enter Hub Name: ")
            vid = input("Enter Vehicle ID: ")
            model = input("Enter Model Name: ")
            battery = int(input("Enter Battery Level: "))

            v = Vehicle(vid, model, battery)
            fleet.add_vehicle_to_hub(hub, v)

        elif choice == "3":
            fleet.view_all_hubs()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
