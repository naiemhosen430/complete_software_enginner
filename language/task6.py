# Task 6: Advanced Concepts


# Write a Python program that demonstrates object-oriented programming:

# 1: Define a class representing a "Car" with attributes like make, model, and year.
# 2: Create an instance of the Car class and print its attributes.
# 3: Define a method in the class to calculate the age of the car.

# Solution
from datetime import datetime as dt

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def all_info(self):
        print(f"Car model name is {self.model}. It has made by {self.make} in {self.year}")
    
    def car_age(self):
        curren_tyear = dt.now().year
        print(f"Car age is {self.year - curren_tyear}")

newCar = Car("Unknown","BMW", 2000)
newCar.all_info()
newCar.car_age()

# completed