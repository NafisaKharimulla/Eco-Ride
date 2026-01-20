import unittest
from models.electric_vehicle import ElectricCar, ElectricScooter

class TestElectricVehicle(unittest.TestCase):

    def test_car_trip_cost(self):
        car = ElectricCar("C1", "Tesla", 90)
        self.assertEqual(car.calculate_trip_cost(10), 10.0)

    def test_scooter_trip_cost(self):
        scooter = ElectricScooter("S1", "Ola", 85)
        self.assertEqual(scooter.calculate_trip_cost(10), 2.5)

    def test_car_str(self):
        car = ElectricCar("C1", "Tesla", 90)
        self.assertIn("Car", str(car))

    def test_scooter_str(self):
        scooter = ElectricScooter("S1", "Ola", 80)
        self.assertIn("Scooter", str(scooter))
