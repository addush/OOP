# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        pass  # To be defined in child classes

# Derived class: Car
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def move(self):
        print(f"{self.brand} {self.model} is Driving 🚗")

# Derived class: Plane
class Plane(Vehicle):
    def __init__(self, brand, model, max_altitude):
        super().__init__(brand, model)
        self.max_altitude = max_altitude
    
    def move(self):
        print(f"{self.brand} {self.model} is Flying ✈️")

# Derived class: Boat
class Boat(Vehicle):
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type
    
    def move(self):
        print(f"{self.brand} {self.model} is Sailing ⛵")

# Using the classes and polymorphism
def main():
    vehicles = [
        Car("Toyota", "Camry", 4),
        Plane("Boeing", "747", 35000),
        Boat("Yamaha", "WaveRunner", "Jet Ski")
    ]
    
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()
