from models import Vehicle, Car, Bicycle



v = Vehicle("Generic", 50, 2010)
car = Car("Toyota", 120, 2020, "Petrol")
bike = Bicycle("Trek", 25, 2022, 18)

vehicles = [v, car, bike]

for obj in vehicles:
    print(obj)              # __str__
    print(obj.info())       # method
    print(obj.move())       # polymorphism
    print()

print(car.refuel())
print(bike.change_gear())

