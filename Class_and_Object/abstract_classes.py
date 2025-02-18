from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @property
    @abstractmethod
    def name(self):
        pass
    
    @name.setter
    @abstractmethod
    def name(self, value):
        pass
    
    @property
    @abstractmethod
    def sound(self):
        pass
    
    @sound.setter
    @abstractmethod
    def sound(self, value):
        pass

# Derived class
class Dog(Animal):
    
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def sound(self):
        return self._sound
    
    @sound.setter
    def sound(self, value):
        self._sound = value

# Another derived class
class Cat(Animal):
    
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def sound(self):
        return self._sound
    
    @sound.setter
    def sound(self, value):
        self._sound = value

# Function to demonstrate polymorphism
def animal_info(animal: Animal):
    print(f"The {animal.name} says {animal.sound}.")

# Create instances
dog = Dog("Dog", "Bark")
cat = Cat("Cat", "Meow")

# Test the behavior
animal_info(dog)  # Output: The Dog says Bark.
animal_info(cat)  # Output: The Cat says Meow.

# Change name and sound
dog.name = "Bulldog"
dog.sound = "Woof"
animal_info(dog)  # Output: The Bulldog says Woof.
