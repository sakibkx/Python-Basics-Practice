# Parent class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle(Brand: {self.brand}, Model: {self.model}, Year: {self.year})"

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, fuel_type):
        super().__init__(brand, model, year)  # Inherit from Vehicle
        self.doors = doors
        self.fuel_type = fuel_type

    def __str__(self):
        return super().__str__() + f", Doors: {self.doors}, Fuel Type: {self.fuel_type}"

# Another Child class inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, year, cc, type_of_bike):
        super().__init__(brand, model, year)  # Inherit from Vehicle
        self.cc = cc
        self.type_of_bike = type_of_bike

    def __str__(self):
        return super().__str__() + f", Engine CC: {self.cc}, Type: {self.type_of_bike}"

# Creating objects
tesla = Car("Tesla", "Model S", 2024, 4, "Electric")
royal_enfield = Bike("Royal Enfield", "Classic 350", 2023, 349, "Cruiser")

# Printing object details using __str__()
print(tesla)
print(royal_enfield)
