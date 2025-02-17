# 🟢 1. Basic For Loops
print("\n--- For loop over a list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n--- For loop with range() ---")
for i in range(5):  # Iterates from 0 to 4
    print("Iteration:", i)

print("\n--- For loop over a tuple ---")
colors = ("red", "green", "blue")
for color in colors:
    print(color)

print("\n--- For loop over a set ---")
unique_numbers = {1, 2, 3, 4}
for num in unique_numbers:
    print(num)

print("\n--- For loop over a dictionary ---")
student = {"name": "Sakib", "age": 21, "dept": "CSE"}
for key, value in student.items():
    print(f"{key}: {value}")


# 🟢 2. While Loop
print("\n--- While loop counting down ---")
count = 5
while count > 0:
    print("Count:", count)
    count -= 1  # Decrement

print("\n--- else with while loop ---")
num = 3
while num > 0:
    print("While loop running:", num)
    num -= 1
else:
    print("While loop finished")


# 🟢 3. Nested Loops
print("\n--- Nested loops: Multiplication table ---")
for i in range(1, 4):  # Rows
    for j in range(1, 4):  # Columns
        print(i * j, end=" ")
    print()  # Newline after each row


# 🟢 4. Loop Control Statements
print("\n--- Break in a loop ---")
for i in range(1, 6):
    if i == 3:
        print("Breaking loop at", i)
        break
    print(i)

print("\n--- Continue in a loop ---")
for i in range(1, 6):
    if i == 3:
        print("Skipping", i)
        continue
    print(i)

print("\n--- else with for loop ---")
for i in range(1, 4):
    print(i)
else:
    print("Loop finished successfully")


# 🟢 5. Pass Statement
print("\n--- Pass statement in a loop ---")
for i in range(5):
    if i == 2:
        pass  # Placeholder, does nothing
    print(i)
