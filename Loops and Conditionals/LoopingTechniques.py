# 1. Using enumerate() - Iterate with index
print("\n--- Using enumerate() ---")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 2. Using zip() - Iterate multiple lists together
print("\n--- Using zip() ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 3. Using items() - Iterate dictionary key-value pairs
print("\n--- Using items() ---")
student = {"name": "Sakib", "age": 21, "dept": "CSE"}
for key, value in student.items():
    print(f"{key}: {value}")

# 4. Using sorted() - Iterate in sorted order
print("\n--- Using sorted() ---")
numbers = [5, 2, 9, 1, 7]
for num in sorted(numbers):
    print(num)

# 5. Using reversed() - Iterate in reverse order
print("\n--- Using reversed() ---")
letters = ["a", "b", "c", "d"]
for letter in reversed(letters):
    print(letter)


