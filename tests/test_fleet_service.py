import unittest
from services.fleet_service import FleetService
from models.electric_vehicle import ElectricCar, ElectricScooter
from unittest.mock import patch, mock_open

class TestFleetService(unittest.TestCase):

    def setUp(self):
        self.fleet = FleetService()
        self.fleet.add_hub("Bangalore")

        self.car = ElectricCar("C1", "Tesla", 90)
        self.scooter = ElectricScooter("S1", "Ola", 85)

    def test_add_vehicle_to_hub(self):
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)
        self.assertEqual(len(self.fleet.hubs["Bangalore"]), 1)

    def test_prevent_duplicate_vehicle(self):
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)
        self.assertEqual(len(self.fleet.hubs["Bangalore"]), 1)

    def test_search_by_hub(self):
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)
        vehicles = self.fleet.search_by_hub("Bangalore")
        self.assertEqual(len(vehicles), 1)

    def test_search_battery_above_80(self):
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)
        self.fleet.add_vehicle_to_hub("Bangalore", self.scooter)

        result = self.fleet.search_battery_above_80()
        self.assertEqual(len(result), 2)

    def test_categorized_view(self):
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)
        self.fleet.add_vehicle_to_hub("Bangalore", self.scooter)

        categorized = self.fleet.categorized_view()
        self.assertEqual(len(categorized["Car"]), 1)
        self.assertEqual(len(categorized["Scooter"]), 1)

    def test_sort_vehicles_by_battery(self):
        car2 = ElectricCar("C2", "BMW", 50)
        self.fleet.add_vehicle_to_hub("Bangalore", car2)
        self.fleet.add_vehicle_to_hub("Bangalore", self.car)

        self.fleet.sort_vehicles_by_battery("Bangalore")
        self.assertEqual(self.fleet.hubs["Bangalore"][0].battery_level, 90)
