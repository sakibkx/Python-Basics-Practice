# 1. Simple if statement
num = 10
if num > 0:
    print("Positive number")

# 2. if-else statement
num = -5
if num > 0:
    print("Positive number")
else:
    print("Negative number or zero")

# 3. if-elif-else statement
num = 0
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("It's zero")

# 4. Nested if statement
num = 15
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# 5. Using multiple conditions with logical operators
age = 25
if age > 18 and age < 30:
    print("Young adult")

# 6. Ternary if statement (short form of if-else)
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print("Number is", result)

# 7. Shorthand if statement (single-line if)
a = 10
if a > 5: print("a is greater than 5")  

# 8. Shorthand if-else statement (single-line if-else)
b = 7
print("Even") if b % 2 == 0 else print("Odd")

# 9. match-case statement (introduced in Python 3.10)
choice = 2

match choice:
    case 1:
        print("You chose option 1")
    case 2:
        print("You chose option 2")
    case 3:
        print("You chose option 3")
    case _:
        print("Invalid choice")

