# Integer
a = 5
print("Integer:", a)

# Float
b = 3.14
print("Float:", b)

# Complex Number
complex_num = 3 + 4j
print("Complex Number:", complex_num)


# Boolean
is_active = True
print("Boolean:", is_active)


# String
name = "Sakib"
print("String:", name)

# List (Mutable ordered collection)
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Tuple (Immutable ordered collection)
coordinates = (10, 20)
print("Tuple:", coordinates)


# Dictionary (Key-Value pairs)
person = {
    "name": "Sakib",
    "age": 21,
    "city": "Rangpur"
}
print("Dictionary:", person)


# NoneType (Represents a null value)
nothing = None
print("NoneType:", nothing)


# Set (Unordered collection of unique elements)
unique_numbers = {1, 2, 3, 4, 5}
print("Set:", unique_numbers)

# Frozenset (Immutable Set)
frozen_set_data = frozenset([1, 2, 3, 4])
print("Frozenset:", frozen_set_data)


# Bytes (Immutable sequence of bytes)
byte_data = b"Hello"
print("Bytes:", byte_data)

# Bytearray (Mutable sequence of bytes)
byte_array_data = bytearray([65, 66, 67])
print("Bytearray:", byte_array_data)

# MemoryView (Mutable sequence of byte array)
byte_array = bytearray('XYZ', 'utf-8')

mv = memoryview(byte_array)

print(mv, mv[0], mv[1], mv[2])
