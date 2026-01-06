from services.fleet_service import FleetService
from models.vehicle import Vehicle


class EcoRideMain:
    def __init__(self):
        self.fleet_service = FleetService()

    def start(self):
        print("Welcome to Eco-Ride Urban Mobility System\n")
        try:
            num = int(input("How many vehicles do you want to add? "))
            for i in range(num):
                print(f"\nEnter details for Vehicle {i + 1}:")
                vehicle_id = input("Vehicle ID: ")
                model = input("Model: ")
                battery_percentage = float(input("Battery Percentage: "))

                vehicle = Vehicle(vehicle_id, model, battery_percentage)
                self.fleet_service.add_vehicle(vehicle)

            print("\nAll Vehicles in the System:")
            for v in self.fleet_service.get_all_vehicles():
                print(v)

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    app = EcoRideMain()
    app.start()

