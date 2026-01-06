from services.fleet_service import FleetService
from models.vehicle import Vehicle
from models.electric_vehicle import ElectricCar, ElectricScooter

class EcoRideMain:
    def __init__(self):
        self.fleet_service = FleetService()

    def start(self):
        print("Welcome to Eco-Ride Urban Mobility System\n")
        try:
            num = int(input("How many vehicles do you want to add? "))
            for i in range(num):
                print(f"\nEnter details for Vehicle {i + 1}:")
                vehicle_type = input("Type (Car/Scooter/ElectricCar/ElectricScooter): ").strip().lower()
                vehicle_id = input("Vehicle ID: ")
                model = input("Model: ")
                battery = float(input("Battery Percentage: "))
                rental_price = float(input("Rental Price: "))
                maintenance_status = input("Maintenance Status (OK/Needs Service/Under Maintenance): ")

                # Create vehicle based on type
                if vehicle_type == "electriccar":
                    seating_capacity = int(input("Seating Capacity: "))
                    vehicle = ElectricCar(vehicle_id, model, battery, seating_capacity)
                elif vehicle_type == "electricscooter":
                    max_speed = float(input("Max Speed Limit (km/h): "))
                    vehicle = ElectricScooter(vehicle_id, model, battery, max_speed)
                else:
                    vehicle = Vehicle(vehicle_id, model, battery)

                vehicle.set_rental_price(rental_price)
                vehicle.set_maintenance_status(maintenance_status)

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
