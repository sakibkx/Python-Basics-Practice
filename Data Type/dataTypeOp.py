# Integer Operations
a = 5
b = 3
print("Integer Operations:")
# Arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)
print("Modulus:", a % b)
# Comparison operations
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# Float Operations
x = 3.14
y = 2.5
print("\nFloat Operations:")
# Arithmetic operations
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Exponentiation:", x ** y)
print("Modulus:", x % y)
# Comparison operations
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)

# String Operations
name = "Sakib"
greeting = "Hello"
print("\nString Operations:")
# Concatenation
print("Concatenation:", greeting + " " + name)
# Repetition
print("Repetition:", name * 2)
# Length of the string
print("Length:", len(name))
# Accessing Character (Indexing)
print("Accessing Character (Indexing):", name[0])
# Slicing (Substring)
print("Slicing (Substring):", name[1:4])
# Convert to Uppercase
print("Uppercase:", name.upper())
# Convert to Lowercase
print("Lowercase:", name.lower())
# Check if a substring exists
print("Check Substring:", "Sak" in name)
# String methods
print("Is Upper:", name.isupper())
print("Is Lower:", name.islower())
print("Starts With 'S':", name.startswith('S'))
print("Ends With 'b':", name.endswith('b'))

#N.B : 

# Original string with escape sequence
string_with_escape = "Hello\nWorld"

# 1️ Normal Print (Interprets Escape Sequence)
print("1️ Normal Print (Interprets \\n as a Newline):")
print(string_with_escape)  
print("-" * 40)

# 2️ Using Raw String (r"...") - Escape sequence is not interpreted
print("2️ Using Raw String (r\"...\"):")
print(r"Hello\nWorld")
print("-" * 40)

# 3️ Using Double Backslashes (\\) to show the actual escape sequence
print("3️ Using Double Backslashes (\\\\):")
print("Hello\\nWorld")
print("-" * 40)

# 4️ Using repr() to display escape sequences as literals
print("4️ Using repr() function:")
print(repr(string_with_escape))
print("-" * 40)

# 5️ Using encode().decode() to show escape sequences explicitly
print("5️ Using encode('unicode_escape').decode():")
print(string_with_escape.encode('unicode_escape').decode())
print("-" * 40)


# List Operations
fruits = ["apple", "banana", "cherry"]
print("\nList Operations:")
# Append an element to the list
fruits.append("orange")
print("Append:", fruits)
# Remove an element from the list
fruits.remove("banana")
print("Remove:", fruits)
# Insert an element at a specific position
fruits.insert(1, "grape")
print("Insert:", fruits)
# Accessing an element from the list
print("Accessing Element:", fruits[0])
# Slicing the list
print("Slicing:", fruits[1:3])
# Get the length of the list
print("Length:", len(fruits))
# Sorting the list alphabetically
fruits.sort()
print("Sort:", fruits)
# Reversing the list
fruits.reverse()
print("Reverse:", fruits)
# Checking membership in the list
print("Contains 'apple':", "apple" in fruits)

# Tuple Operations
coordinates = (10, 20, 30)
print("\nTuple Operations:")
# Accessing an element from the tuple
print("Accessing Element:", coordinates[1])
# Slicing the tuple
print("Slicing:", coordinates[1:3])
# Get the length of the tuple
print("Length:", len(coordinates))
# Count occurrences of a value in a tuple
print("Count of 10:", coordinates.count(10))
# Find index of a value in a tuple
print("Index of 20:", coordinates.index(20))

# Set Operations
unique_numbers = {1, 2, 3, 4, 5}
print("\nSet Operations:")
# Add an element to the set
unique_numbers.add(6)
print("Add:", unique_numbers)
# Remove an element from the set
unique_numbers.remove(3)
print("Remove:", unique_numbers)
# Union of two sets (all unique elements from both sets)
print("Set Union:", unique_numbers | {7, 8})
# Intersection of two sets (common elements between sets)
print("Set Intersection:", unique_numbers & {4, 5, 6})
# Difference between two sets (elements in the first set but not in the second)
print("Set Difference:", unique_numbers - {4, 5})
# Symmetric Difference (elements in either set, but not both)
print("Symmetric Difference:", unique_numbers ^ {4, 5, 6})

# Dictionary Operations
person = {
    "name": "Sakib",
    "age": 21,
    "city": "Rangpur"
}
print("\nDictionary Operations:")
# Access value by key
print("Access Value by Key:", person["name"])
# Modify the value associated with a key
person["age"] = 22
print("Modify:", person)
# Add a new key-value pair
person["country"] = "Bangladesh"
print("Add:", person)
# Delete a key-value pair from the dictionary
del person["city"]
print("Delete:", person)
# Check if a key exists
print("Contains 'name':", "name" in person)
# Get all keys and values
print("Keys:", person.keys())
print("Values:", person.values())
# Get items (key-value pairs)
print("Items:", person.items())

# NoneType Operations
nothing = None
print("\nNoneType Operations:")
# Check if a variable is None
print("Is None:", nothing is None)

# Complex Number Operations
complex_num = 3 + 4j
print("\nComplex Number Operations:")
# Arithmetic operations
print("Addition:", complex_num + (1 + 2j))
print("Subtraction:", complex_num - (1 + 2j))
print("Multiplication:", complex_num * (1 + 2j))
print("Division:", complex_num / (1 + 2j))
# Get the conjugate of a complex number
print("Conjugate:", complex_num.conjugate())
# Get the real part of a complex number
print("Real Part:", complex_num.real)
# Get the imaginary part of a complex number
print("Imaginary Part:", complex_num.imag)
# Absolute value of a complex number (magnitude)
print("Absolute Value:", abs(complex_num))

# Bytes and Bytearray Operations
byte_data = b"Hello"
byte_array_data = bytearray([65, 66, 67])
print("\nBytes & Bytearray Operations:")
# Get the length of a bytes object
print("Byte Length:", len(byte_data))
# Access individual byte (indexing)
print("Byte Indexing:", byte_data[0])
# Modify a bytearray
byte_array_data.append(68)
print("Bytearray Append:", byte_array_data)
# Modify the content of a bytearray
byte_array_data[0] = 72
print("Bytearray Modify:", byte_array_data)
# Convert bytearray to string
print("Bytearray to String:", byte_array_data.decode())
# Convert string to bytes
print("String to Bytes:", "Hello".encode())

# Frozenset Operations
frozen_set_data = frozenset([1, 2, 3, 4])
print("\nFrozenset Operations:")
# Perform union with another frozenset
print("Frozenset Union:", frozen_set_data | frozenset([5, 6]))
# Perform intersection with another frozenset
print("Frozenset Intersection:", frozen_set_data & frozenset([3, 4, 5]))
# Perform difference with another frozenset
print("Frozenset Difference:", frozen_set_data - frozenset([2, 3]))
