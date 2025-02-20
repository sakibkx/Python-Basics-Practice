from collections import Counter

# 1. Creating a Counter from a list
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter1 = Counter(data)
print("Counter from list:", counter1)

# 2. Creating a Counter from a string
text = "hello world"
counter2 = Counter(text)
print("Counter from string:", counter2)

# 3. Accessing element counts
print("Count of 'l':", counter2['l'])
print("Count of 'z' (not present):", counter2['z'])  # Returns 0

# 4. Updating a Counter
counter1.update([3, 4, 4, 5, 5, 5])
print("Updated Counter:", counter1)

# 5. Using most_common()
print("Most common elements:", counter1.most_common(2))

# 6. Using elements() to expand the Counter
print("Expanded elements:", list(counter1.elements()))

# 7. Subtracting elements
counter3 = Counter([2, 3, 3, 4, 5])
counter1.subtract(counter3)
print("After subtraction:", counter1)

# 8. Arithmetic Operations
counterA = Counter([1, 2, 2, 3])
counterB = Counter([2, 3, 3, 4])

print("Addition (Union):", counterA + counterB)  
print("Subtraction:", counterA - counterB)  
print("Intersection:", counterA & counterB)  
print("Union (max counts):", counterA | counterB)  
