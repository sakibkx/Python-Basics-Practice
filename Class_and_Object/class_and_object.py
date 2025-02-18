# 1. Classes and Objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Car: {self.brand} {self.model}"

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.display_info())  # Output: Car: Toyota Corolla
print(car2.display_info())  # Output: Car: Honda Civic

# ----------------------------------------

# 2. Class and Instance Variables
class Student:
    school = "XYZ High School"  # Class variable

    def __init__(self, name, grade):
        self.name = name  # Instance variable
        self.grade = grade

s1 = Student("Alice", "A")
s2 = Student("Bob", "B")

print(s1.school)  # Output: XYZ High School
print(s2.school)  # Output: XYZ High School
print(s1.name, s1.grade)  # Output: Alice A
print(s2.name, s2.grade)  # Output: Bob B

# ----------------------------------------

# 3. __init__ Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Charlie", 30)
print(p.name, p.age)  # Output: Charlie 30

# ----------------------------------------

# 4. __str__ Method
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python Basics")
print(b)  # Output: Book: Python Basics

# ----------------------------------------

# 5. __len__ Method
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song1", "Song2", "Song3"])
print(len(p))  # Output: 3

# ----------------------------------------

# 6. self Parameter
class Animal:
    def __init__(self, name):
        self.name = name  # self refers to the current instance

    def speak(self):
        return f"{self.name} makes a sound"

a = Animal("Dog")
print(a.speak())  # Output: Dog makes a sound
