# Base class
class Vehicle:
    def __init__(self, fuel_type, transmission, wheels, max_speed):
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.wheels = wheels
        self.max_speed = max_speed

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

    def vehicle_info(self):
        print("Fuel Type:", self.fuel_type)
        print("Transmission:", self.transmission)
        print("Wheels:", self.wheels)
        print("Max Speed:", self.max_speed)
        print()


# Child class Car
class Car(Vehicle):
    def __init__(self, fuel_type, transmission, max_speed, air_conditioner):
        super().__init__(fuel_type, transmission, 4, max_speed)
        self.air_conditioner = air_conditioner

    def brand(self):
        print("Car Brand: Toyota")


# Child class Bike
class Bike(Vehicle):
    def __init__(self, fuel_type, transmission, max_speed, bike_type):
        super().__init__(fuel_type, transmission, 2, max_speed)
        self.bike_type = bike_type

    def brand(self):
        print("Bike Brand: Yamaha")


# Creating objects
car1 = Car("Petrol", "Automatic", "180 km/h", True)
car2 = Car("Diesel", "Manual", "160 km/h", False)

bike1 = Bike("Petrol", "Manual", "120 km/h", "Sports")
bike2 = Bike("Electric", "Automatic", "90 km/h", "Scooter")

# Using objects
vehicles = [car1, car2, bike1, bike2]

for v in vehicles:
    v.brand()
    v.vehicle_info()
    v.start()
    v.stop()
    print("----------------------")
