class Vehicle:
    def __init__(self, brand, speed, year):
        self.brand = brand
        self.speed = speed
        self.year = year

    def move(self):
        return f"{self.brand} is moving at {self.speed} km/h"

    def info(self):
        return f"{self.brand}, {self.year}"

    def __str__(self):
        return f"Vehicle(brand={self.brand}, speed={self.speed}, year={self.year})"

class Car(Vehicle):
    def __init__(self, brand, speed, year, fuel_type):
        super().__init__(brand, speed, year)
        self.fuel_type = fuel_type

    def move(self):  # override
        return f"{self.brand} car drives on the road at {self.speed} km/h"

    def refuel(self):
        return f"{self.brand} uses {self.fuel_type}"

    def __str__(self):
        return f"Car(brand={self.brand}, speed={self.speed}, year={self.year}, fuel={self.fuel_type})"

class Bicycle(Vehicle):
    def __init__(self, brand, speed, year, gear_count):
        super().__init__(brand, speed, year)
        self.gear_count = gear_count

    def move(self):  # override
        return f"{self.brand} bicycle is pedaling at {self.speed} km/h"

    def change_gear(self):
        return f"{self.brand} has {self.gear_count} gears"

    def __str__(self):
        return f"Bicycle(brand={self.brand}, speed={self.speed}, year={self.year}, gears={self.gear_count})"