# 1. Direct Recursion: A function that calls itself
def direct_recursion(n):
    if n <= 0:
        return 0
    return n + direct_recursion(n - 1)

print("Direct Recursion (Sum of first 5 numbers):", direct_recursion(5))  # Output: 15


# 2. Indirect Recursion: Function A calls function B, and function B calls function A
def function_a(n):
    if n <= 0:
        return 0
    return function_b(n - 1)

def function_b(n):
    if n <= 0:
        return 0
    return function_a(n - 1)

print("Indirect Recursion (n=3):", function_a(3))  # Output: 0 (base case is eventually reached)


# 3. Tail Recursion: The recursive call is the last thing that happens in the function
def tail_recursion(n, accumulator=0):
    if n == 0:
        return accumulator
    return tail_recursion(n - 1, accumulator + n)

print("Tail Recursion (Sum of first 5 numbers):", tail_recursion(5))  # Output: 15


# 4. Fibonacci Sequence Using Recursion (Direct Recursion Example)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 5:", fibonacci(5))  # Output: 5


# 5. Factorial Using Recursion (Direct Recursion Example)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: 120


# 6. Finding the Greatest Common Divisor (GCD) Using Recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6
