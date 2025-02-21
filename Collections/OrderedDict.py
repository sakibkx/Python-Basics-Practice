from collections import OrderedDict

# Creating an OrderedDict
od = OrderedDict()
od['apple'] = 3
od['banana'] = 5
od['cherry'] = 2

# Printing initial dictionary
print("Initial OrderedDict:")
for key, value in od.items():
    print(key, value)

# Changing a value
od['banana'] = 10
print("\nAfter updating 'banana':")
for key, value in od.items():
    print(key, value)

# Moving 'apple' to the end
od.move_to_end('apple')
print("\nAfter moving 'apple' to the end:")
for key, value in od.items():
    print(key, value)

# Moving 'cherry' to the beginning
od.move_to_end('cherry', last=False)
print("\nAfter moving 'cherry' to the beginning:")
for key, value in od.items():
    print(key, value)

# Removing the last item
od.popitem()
print("\nAfter removing the last item:")
for key, value in od.items():
    print(key, value)

# Removing the first item
od.popitem(last=False)
print("\nAfter removing the first item:")
for key, value in od.items():
    print(key, value)
