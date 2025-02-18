# Method Overriding (Runtime Polymorphism)
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

# Demonstrating Method Overriding
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())  # Calls the overridden method in respective classes

print("-" * 50)

# Method Overloading (Pythonic Way)
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c  # Default argument acts like overloading

math_op = MathOperations()
print(math_op.add(5, 10))    # Output: 15 (two parameters)
print(math_op.add(5, 10, 15)) # Output: 30 (three parameters)

print("-" * 50)

# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)  # Overloading '+' operator

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Uses operator overloading
print(p3)  # Output: Point(6, 8)

print("-" * 50)

# Duck Typing Example
class Car:
    def start(self):
        return "Car is starting"

class Bike:
    def start(self):
        return "Bike is starting"

class Bus:
    def start(self):
        return "Bus is starting"

# Function that works with any object that has a 'start' method
def vehicle_start(vehicle):
    print(vehicle.start())

vehicle_start(Car())   # Output: Car is starting
vehicle_start(Bike())  # Output: Bike is starting
vehicle_start(Bus())   # Output: Bus is starting
