# 1️ Using f-strings (Python 3.6+)
name = "Sakib"
age = 21
pi = 3.14159

print("1️ Using f-strings:")
print(f"My name is {name} and I am {age} years old.")
print(f"Value of Pi up to 2 decimal places: {pi:.2f}")  # Formatting float
print(f"Binary of 10: {10:b}, Hex: {255:x}, Octal: {64:o}")  # Number formatting
print(f"Right-aligned: {'Hello':>10}, Left-aligned: {'World':<10}, Centered: {'Python':^10}")
print("-" * 40)

# 2️ Using .format() method
print("2️ Using .format() method:")
print("My name is {} and I am {} years old.".format(name, age))
print("Pi to 3 decimal places: {:.3f}".format(pi))
print("Binary: {:b}, Hex: {:x}, Octal: {:o}".format(10, 255, 64))
print("Right: {:>10}, Left: {:<10}, Centered: {:^10}".format("Hello", "World", "Python"))
print("-" * 40)

# 3️ Using Old-style % formatting
print("3️ Using Old-style % formatting:")
print("My name is %s and I am %d years old." % (name, age))
print("Pi to 4 decimal places: %.4f" % pi)
print("Binary: %b is not supported in old-style formatting")  # No binary in old-style formatting
print("Right: %10s, Left: %-10s, Centered: %10s" % ("Hello", "World", "Python"))
print("-" * 40)

# 4️ String alignment with f-strings
print("4️ String Alignment:")
print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")
print(f"{'Python':<10} | {'Programming':^10} | {'Language':>10}")
print("-" * 40)

# 5️ Number formatting
num = 1234567.89123
print("5️ Number Formatting:")
print(f"Comma separator: {num:,}")
print(f"Scientific notation: {num:.2e}")
print(f"Percentage: {0.857:.2%}")  # 85.7%
print("-" * 40)

# 6️ Padding numbers with zeros
print("6️ Padding Numbers:")
print(f"Padded Number: {42:05d}")  # Outputs: 00042
print(f"Hex with prefix: {255:#x}, Octal with prefix: {64:#o}")
print("-" * 40)

# 7️ Dynamic width formatting
width = 10
print(f"Dynamic Width: {'Hello':{width}}World!")
print("-" * 40)
