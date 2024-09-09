"""
Name: Seth Deno
File Name: ListFunctionClass.py
Description: The program will take vehicle information from the user and output
this information to them in a easy to read format.
"""

# Parent class to Automobile class
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

# Child class of Vehicle class
class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# This block of code gathers input from user 
vehicle_type = input("Please enter your vehicle type: ")
vehicle_year = input("Please enter your vehicle year: ")
vehicle_make = input("Please enter your vehicle make: ")
vehicle_model = input("Please enter your vehicle model: ")
vehicle_doors = input("Please enter the number of doors (2 or 4) your vehcile has: ")
vehicle_roof = input("Please enter the type of roof (solid or sun roof) your vehicle has: ")

vehicleOutput = Automobile(vehicle_type, vehicle_year, vehicle_make, vehicle_model, vehicle_doors, vehicle_roof) # This creates a class object

# This block of code outputs vehicle information in a easy to read format 
print("Vehicle type:", vehicleOutput.vehicleType)
print("Year:", vehicleOutput.year)
print("Make:", vehicleOutput.make)
print("Model:", vehicleOutput.model)
print("Number of doors:", vehicleOutput.doors)
print("Type of roof:", vehicleOutput.roof)