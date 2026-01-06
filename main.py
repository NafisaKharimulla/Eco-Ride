from services.fleet_service import FleetService
from models.vehicle import ElectricCar, ElectricScooter


def main():
    print("Welcome to Eco-Ride Urban Mobility System")

    fleet = FleetService()

    while True:
        print("\n1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            hub = input("Enter hub name: ")
            fleet.add_hub(hub)

        elif choice == "2":
            hub = input("Enter hub name: ")

            vtype = input("Enter vehicle type (car/scooter): ").lower()
            vid = input("Enter vehicle ID: ")
            model = input("Enter model name: ")
            battery = int(input("Enter battery percentage: "))

            if vtype == "car":
                seats = int(input("Enter seating capacity: "))
                vehicle = ElectricCar(vid, model, battery, seats)

            elif vtype == "scooter":
                speed = int(input("Enter max speed: "))
                vehicle = ElectricScooter(vid, model, battery, speed)

            else:
                print("Invalid vehicle type")
                continue

            fleet.add_vehicle_to_hub(hub, vehicle)

        elif choice == "3":
            fleet.view_all_hubs()

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
