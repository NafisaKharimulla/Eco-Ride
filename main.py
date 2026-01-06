from models.electric_vehicle import ElectricCar, ElectricScooter
from services.fleet_service import FleetService


def main():
    print("Welcome to Eco-Ride Urban Mobility System")

    fleet = FleetService()

    num = int(input("\nHow many vehicles do you want to add? "))

    for i in range(num):
        print(f"\nEnter details for Vehicle {i + 1}")

        v_type = input("Type (car/scooter): ").strip().lower()
        vehicle_id = input("Vehicle ID: ")
        model = input("Model: ")
        battery = float(input("Battery Percentage: "))

        if v_type == "car":
            seats = int(input("Seating Capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)

        elif v_type == "scooter":
            speed = float(input("Max Speed Limit (km/h): "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)

        else:
            print("Invalid vehicle type. Skipping entry.")
            continue

        fleet.add_vehicle(vehicle)

    print("\n--- Vehicle List ---")
    for v in fleet.get_all_vehicles():
        print(v)

    print("\n--- Trip Cost Calculation (Polymorphism in action) ---")

    for v in fleet.get_all_vehicles():
        print(f"\nVehicle: {v}")

        if isinstance(v, ElectricCar):
            distance = float(input("Enter trip distance in km: "))
            cost = v.calculate_trip_cost(distance)
            print(f"Trip Cost = ${cost:.2f}")

        elif isinstance(v, ElectricScooter):
            minutes = float(input("Enter ride duration in minutes: "))
            cost = v.calculate_trip_cost(minutes)
            print(f"Trip Cost = ${cost:.2f}")


if __name__ == "__main__":
    main()
