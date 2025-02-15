# Integer to other types
int_num = 10
print("Integer to Other Types:")
# Integer to Float
float_from_int = float(int_num)
print(f"Integer to Float: {int_num} -> {float_from_int}")
# Integer to String
str_from_int = str(int_num)
print(f"Integer to String: {int_num} -> {str_from_int}")
# Integer to Complex
complex_from_int = complex(int_num)
print(f"Integer to Complex: {int_num} -> {complex_from_int}")

# Float to other types
float_num = 3.14
print("\nFloat to Other Types:")
# Float to Integer (Truncates the decimal part)
int_from_float = int(float_num)
print(f"Float to Integer: {float_num} -> {int_from_float}")
# Float to String
str_from_float = str(float_num)
print(f"Float to String: {float_num} -> {str_from_float}")
# Float to Complex
complex_from_float = complex(float_num)
print(f"Float to Complex: {float_num} -> {complex_from_float}")

# String to other types
str_num = "25"
print("\nString to Other Types:")
# String to Integer
int_from_str = int(str_num)
print(f"String to Integer: '{str_num}' -> {int_from_str}")
# String to Float
float_from_str = float(str_num)
print(f"String to Float: '{str_num}' -> {float_from_str}")
# String to Complex
complex_from_str = complex(str_num)
print(f"String to Complex: '{str_num}' -> {complex_from_str}")

# Complex to other types
complex_num = 4 + 3j
print("\nComplex to Other Types:")
# Complex to String
str_from_complex = str(complex_num)
print(f"Complex to String: {complex_num} -> {str_from_complex}")
# Complex to Float or Integer is not directly possible, but we can get the real or imaginary parts:
real_from_complex = complex_num.real
imag_from_complex = complex_num.imag
print(f"Real Part of Complex: {complex_num} -> {real_from_complex}")
print(f"Imaginary Part of Complex: {complex_num} -> {imag_from_complex}")

# List to other types
list_data = [1, 2, 3]
print("\nList to Other Types:")
# List to String (joining the elements as a string)
str_from_list = ''.join(map(str, list_data))
print(f"List to String: {list_data} -> {str_from_list}")
# List to Tuple
tuple_from_list = tuple(list_data)
print(f"List to Tuple: {list_data} -> {tuple_from_list}")
# List to Set
set_from_list = set(list_data)
print(f"List to Set: {list_data} -> {set_from_list}")

# Tuple to other types
tuple_data = (1, 2, 3)
print("\nTuple to Other Types:")
# Tuple to List
list_from_tuple = list(tuple_data)
print(f"Tuple to List: {tuple_data} -> {list_from_tuple}")
# Tuple to Set
set_from_tuple = set(tuple_data)
print(f"Tuple to Set: {tuple_data} -> {set_from_tuple}")
# Tuple to String (joining the elements as a string)
str_from_tuple = ''.join(map(str, tuple_data))
print(f"Tuple to String: {tuple_data} -> {str_from_tuple}")

# Set to other types
set_data = {1, 2, 3}
print("\nSet to Other Types:")
# Set to List
list_from_set = list(set_data)
print(f"Set to List: {set_data} -> {list_from_set}")
# Set to Tuple
tuple_from_set = tuple(set_data)
print(f"Set to Tuple: {set_data} -> {tuple_from_set}")
# Set to String (joining the elements as a string)
str_from_set = ''.join(map(str, set_data))
print(f"Set to String: {set_data} -> {str_from_set}")

# Dictionary to other types
dict_data = {"name": "Sakib", "age": 21}
print("\nDictionary to Other Types:")
# Dictionary to List of Tuples (Key-Value Pairs)
list_from_dict = list(dict_data.items())
print(f"Dictionary to List of Tuples: {dict_data} -> {list_from_dict}")
# Dictionary to String (Keys and Values concatenated)
str_from_dict = str(dict_data)
print(f"Dictionary to String: {dict_data} -> {str_from_dict}")

# NoneType to other types
none_data = None
print("\nNoneType to Other Types:")
# None to String
str_from_none = str(none_data)
print(f"NoneType to String: {none_data} -> {str_from_none}")
# None to Integer (will cause an error)
# int_from_none = int(none_data)  # Uncommenting this line will raise a TypeError

# Bytes and Bytearray to other types
bytes_data = b"Hello"
bytearray_data = bytearray([65, 66, 67])
print("\nBytes and Bytearray to Other Types:")
# Bytes to String
str_from_bytes = bytes_data.decode()
print(f"Bytes to String: {bytes_data} -> {str_from_bytes}")
# Bytearray to String
str_from_bytearray = bytearray_data.decode()
print(f"Bytearray to String: {bytearray_data} -> {str_from_bytearray}")
# Bytearray to List
list_from_bytearray = list(bytearray_data)
print(f"Bytearray to List: {bytearray_data} -> {list_from_bytearray}")

# Frozenset to other types
frozenset_data = frozenset([1, 2, 3])
print("\nFrozenset to Other Types:")
# Frozenset to List
list_from_frozenset = list(frozenset_data)
print(f"Frozenset to List: {frozenset_data} -> {list_from_frozenset}")
# Frozenset to Set
set_from_frozenset = set(frozenset_data)
print(f"Frozenset to Set: {frozenset_data} -> {set_from_frozenset}")
