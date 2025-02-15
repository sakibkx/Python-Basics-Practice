# Printing multiple values
print("My name is", "Sakib")

# Multi Printing
word = "eye"
times=5
print(word*times)

# Using f-string for formatted output
name = "Sakib"
age = 21
print(f"My name is {name} and I am {age} years old.")

# Printing numbers and expressions
print("The sum of 5 and 3 is", 5 + 3)

# Printing with separators
print("Python", "is", "awesome", sep="-")

# Printing with end parameter
print("This is line one.", end=" ")
print("This is line two.")

# Printing a multiline string
print("""This is a
multiline string
using triple quotes.""")

# Using escape characters
print("I am learning Python.\nIt's fun!")


# 1. Formatting Output using The Format Method
name = "Sakib"
age = 21
cgpa = 3.75

print("My name is {}, I am {} years old, and my CGPA is {:.2f}.".format(name, age, cgpa))

# 2. Advanced Usage with Positional and Named Parameters
# Positional Arguments
print("My name is {0}, I am {1} years old, and my CGPA is {2:.2f}.".format(name, age, cgpa))

# Named Arguments
print("My name is {n}, I am {a} years old, and my CGPA is {c:.2f}.".format(n=name, a=age, c=cgpa))

# Mixing Positional and Named Arguments
print("I am {0}, my CGPA is {c}, and my age is {1}.".format(name, age, c=cgpa))

# Reordering Indexes
print("{2} is my CGPA, {0} is my name, and I am {1} years old.".format(name, age, cgpa))

# 3. Formatting Output using The String Method
# Using str.ljust(), str.rjust(), and str.center() for alignment
print("Name".ljust(10), "Age".rjust(3), "CGPA".center(6))
print("-" * 25)
print(name.ljust(10), str(age).rjust(3), str(cgpa).center(6))

# 4. Python’s Format Conversion Rule
num = 255
print("Decimal: {}".format(num))  # Default decimal
print("Binary: {:b}".format(num))  # Binary
print("Octal: {:o}".format(num))   # Octal
print("Hexadecimal (lowercase): {:x}".format(num))  # Hexadecimal (lowercase)
print("Hexadecimal (uppercase): {:X}".format(num))  # Hexadecimal (uppercase)

# Using !r, !s, and !a for string conversion
string = "Hello"
print("Using !r: {!r}".format(string))  # Shows how Python represents the string
print("Using !s: {!s}".format(string))  # Default string representation
print("Using !a: {!a}".format(string))  # ASCII representation

# Floating-point formatting
pi = 3.1415926535
print("Pi with 2 decimal places: {:.2f}".format(pi))
print("Pi in scientific notation: {:.3e}".format(pi))
print("Pi in percentage format: {:.2%}".format(pi / 10))


