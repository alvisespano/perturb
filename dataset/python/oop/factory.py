from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle"

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()

def test():
    vehicle_type = input("Enter the type of vehicle you want to create (car/motorcycle): ").strip().lower()
    if vehicle_type == "car":
        factory = CarFactory()
    elif vehicle_type == "motorcycle":
        factory = MotorcycleFactory()
    else:
        exit()

    vehicle = factory.create_vehicle()

    print(vehicle.drive())
