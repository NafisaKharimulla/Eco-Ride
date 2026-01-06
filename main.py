from services.fleet_service import FleetService
from models.vehicle import ElectricCar, ElectricScooter


def main():
    print("Welcome to Eco-Ride Urban Mobility System")

    fleet = FleetService()

    while True:
        print("\n1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Search Vehicles by Hub")
        print("5. Search Vehicles with Battery > 80%")
        print("6. Calculate Trip Cost (Polymorphism Demo)")
        print("7. Exit")

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
            hub = input("Enter hub name to search: ")
            fleet.search_by_hub(hub)

        elif choice == "5":
            fleet.search_by_battery()

        #  UC-5 Polymorphism
        elif choice == "6":
            vtype = input("Enter vehicle type (car/scooter): ").lower()

            if vtype == "car":
                distance = float(input("Enter distance (km): "))
                cost = ElectricCar("temp", "demo", 100, 4).calculate_trip_cost(distance)
                print(f"Trip Cost = ₹{cost}")

            elif vtype == "scooter":
                minutes = float(input("Enter trip time (minutes): "))
                cost = ElectricScooter("temp", "demo", 100, 40).calculate_trip_cost(minutes)
                print(f"Trip Cost = ₹{cost}")

            else:
                print("Invalid vehicle type")

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
