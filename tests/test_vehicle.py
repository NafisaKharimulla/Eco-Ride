import unittest
from models.electric_vehicle import ElectricCar

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = ElectricCar("V1", "Tesla", 90)

    def test_battery_level_validation(self):
        with self.assertRaises(ValueError):
            ElectricCar("V2", "Tesla", 150)

    def test_get_and_set_status(self):
        self.vehicle.set_status("On Trip")
        self.assertEqual(self.vehicle.get_status(), "On Trip")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.vehicle.set_status("Flying")

    def test_vehicle_equality(self):
        v1 = ElectricCar("V1", "Tesla", 80)
        v2 = ElectricCar("V1", "BMW", 60)
        self.assertEqual(v1, v2)
