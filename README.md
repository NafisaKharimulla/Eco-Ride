# Urban Mobility & Fleet Management System (Eco-Ride)

Eco-Ride is a Python-based Urban Mobility & Fleet Management System designed to simulate real-world electric vehicle fleet operations. The project demonstrates strong implementation of Object-Oriented Programming (OOP) principles, data integrity, file handling, and system design best practices.

---

## Learning Outcomes

This project demonstrates the ability to:

1. Apply OOP Pillars:
   - Encapsulation
   - Inheritance
   - Abstraction
   - Polymorphism

2. Work with Python Collections & Dictionaries  
   - Manage fleet hubs and vehicle records

3. Implement File I/O Operations  
   - Store and retrieve data using CSV and JSON files

4. Ensure Data Integrity  
   - Duplicate checks
   - Advanced sorting and filtering

5. Implement Exception Handling  
   - Maintain robust and user-friendly system interaction

---

##  Program Flow

- Displays: **"Welcome to Eco-Ride Urban Mobility System"**
- Main execution handled in `EcoRideMain` class (Master branch)
- Each Use Case (UC) implemented in a separate Git branch
- Proper naming conventions, indentation, and clean code maintained

---

#  Use Case Implementation Details

---

##  UC 1: Basic Fleet Setup

- Created `Vehicle` class
- Constructor initializes:
  - `vehicle_id`
  - `model`
  - `battery_percentage`

---

##  UC 2: Encapsulation & Security

- Private attributes:
  - `__maintenance_status`
  - `__rental_price`
- Implemented getters and setters
- Added validation:
  - Battery percentage must be between 0 and 100

---

##  UC 3: Inheritance & Specialization

Created child classes:

- `ElectricCar`
  - Additional attribute: `seating_capacity`

- `ElectricScooter`
  - Additional attribute: `max_speed_limit`

Used `super().__init__()` for parent initialization reuse.

---

##  UC 4: Abstraction (Contract Enforcement)

- Used `abc` module
- Converted `Vehicle` into Abstract Base Class (ABC)
- Defined abstract method:

```python
calculate_trip_cost(distance)
```

All vehicle types must implement this method.

---

##  UC 5: Polymorphism in Action

Overridden `calculate_trip_cost()`:

- ElectricCar  
  `$5.00 base + $0.50 per km`

- ElectricScooter  
  `$1.00 base + $0.15 per minute`

Demonstrated dynamic behavior using a list of mixed vehicle objects.

---

##  UC 6: Fleet Management (Multiple Hubs)

- Managed multiple hubs (e.g., Downtown, Airport)
- Used Dictionary:
  
```
{
  "Downtown": [Vehicle1, Vehicle2],
  "Airport": [Vehicle3]
}
```

- Console-based hub and vehicle management

---

##  UC 7: Data Integrity & Equality

- Prevented duplicate Vehicle IDs within a hub
- Overrode `__eq__()` method
- Used list comprehension / filters for duplicate detection

---

##  UC 8: Search Functionality

- Search vehicles by:
  - Hub Location
  - Battery Status (> 80%)
- Used lambda functions and filters

---

##  UC 9: Categorized View

- Grouped vehicles by Type:
  - Cars
  - Scooters
- Maintained dictionary mapping type → vehicle objects

---

##  UC 10: Fleet Analytics

Generated summary:

- Total Available vehicles
- Total On Trip vehicles
- Total Under Maintenance vehicles

Displayed formatted analytics report.

---

## UC 11: Alphabetical Sorting

- Sorted vehicles by Model Name
- Used:
  - `sort()` or `sorted()`
- Overrode `__str__()` for clean console output

---

##  UC 12: Advanced Sorting

- Sorted by:
  - Battery Level (descending)
  - Fare Price
- Used lambda keys

---

##  UC 13: File I/O – CSV Persistence

- Used Python `csv` module
- Saved fleet records to CSV
- Loaded records on system startup

---

## UC 14: File I/O – JSON Integration

- Used Python `json` module
- Stored nested Hub-Vehicle structure
- Implemented object serialization/deserialization

---

#  Technologies Used

- Python 3.x
- OOP Concepts
- abc Module
- csv Module
- json Module
- Exception Handling
- Git & Git Branching

---

#  Suggested Project Structure

```
EcoRide/
│
├── main.py
├── vehicle.py
├── electric_car.py
├── electric_scooter.py
├── fleet_manager.py
├── data/
│   ├── fleet.csv
│   └── fleet.json
└── README.md
```

---

#  Key Concepts Demonstrated

- Object-Oriented Programming
- Real-world system modeling
- Data validation & integrity
- Modular design
- Clean code practices
- Branch-based development workflow

---

#  Author

Nafisa Shaik  
Python Developer | OOP Enthusiast | Urban Mobility Systems Explorer  

---

 If you found this project useful, consider giving it a star!
