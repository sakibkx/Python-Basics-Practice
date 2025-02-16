# Global Scope
global_var = "I am Global"  # Declared outside all functions

def global_scope_example():
    print("Accessing global variable inside function:", global_var)

global_scope_example()
print("Accessing global variable outside function:", global_var)
print("-" * 50)

# Local Scope
def local_scope_example():
    local_var = "I am Local"  # Declared inside the function
    print("Accessing local variable inside function:", local_var)

local_scope_example()
# print(local_var)  # This will give an error because local_var is not accessible outside
print("-" * 50)

# Enclosing Scope (Nonlocal)
def outer_function():
    enclosing_var = "I am Enclosing"

    def inner_function():
        nonlocal enclosing_var  # Refers to the outer function's variable
        enclosing_var = "Modified by Inner Function"
        print("Accessing enclosing variable inside inner function:", enclosing_var)

    inner_function()
    print("Accessing enclosing variable after modification:", enclosing_var)

outer_function()
print("-" * 50)

# Modifying Global Variables using `global`
count = 0

def modify_global():
    global count  # Declaring that we want to modify the global variable
    count += 1
    print("Modified global variable inside function:", count)

modify_global()
print("Modified global variable outside function:", count)
print("-" * 50)

# Built-in Scope
print("Accessing built-in function:", len("Hello"))  # `len()` is from Python's built-in scope
