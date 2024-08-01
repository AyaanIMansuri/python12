# Python program to demonstrate type conversion

# Converting string to integer
str_num = "123"
int_num = int(str_num)
print("String to Integer:")
print(f"Original string: {str_num} (type: {type(str_num)})")
print(f"Converted to integer: {int_num} (type: {type(int_num)})\n")

# Converting string to float
str_float = "123.45"
float_num = float(str_float)
print("String to Float:")
print(f"Original string: {str_float} (type: {type(str_float)})")
print(f"Converted to float: {float_num} (type: {type(float_num)})\n")

# Converting integer to float
int_num = 123
float_num = float(int_num)
print("Integer to Float:")
print(f"Original integer: {int_num} (type: {type(int_num)})")
print(f"Converted to float: {float_num} (type: {type(float_num)})\n")

# Converting float to integer
float_num = 123.45
int_num = int(float_num)
print("Float to Integer:")
print(f"Original float: {float_num} (type: {type(float_num)})")
print(f"Converted to integer: {int_num} (type: {type(int_num)})\n")

# Converting integer to string
int_num = 123
str_num = str(int_num)
print("Integer to String:")
print(f"Original integer: {int_num} (type: {type(int_num)})")
print(f"Converted to string: {str_num} (type: {type(str_num)})\n")

# Converting float to string
float_num = 123.45
str_float = str(float_num)
print("Float to String:")
print(f"Original float: {float_num} (type: {type(float_num)})")
print(f"Converted to string: {str_float} (type: {type(str_float)})\n")

# Converting string to list
str_list = "Hello"
list_str = list(str_list)
print("String to List:")
print(f"Original string: {str_list} (type: {type(str_list)})")
print(f"Converted to list: {list_str} (type: {type(list_str)})\n")

# Converting list to string
list_str = ['H', 'e', 'l', 'l', 'o']
str_list = ''.join(list_str)
print("List to String:")
print(f"Original list: {list_str} (type: {type(list_str)})")
print(f"Converted to string: {str_list} (type: {type(str_list)})\n")

# Converting integer to boolean
int_num = 0
bool_val = bool(int_num)
print("Integer to Boolean:")
print(f"Original integer: {int_num} (type: {type(int_num)})")
print(f"Converted to boolean: {bool_val} (type: {type(bool_val)})\n")

# Converting string to boolean
str_val = ""
bool_val = bool(str_val)
print("String to Boolean:")
print(f"Original string: '{str_val}' (type: {type(str_val)})")
print(f"Converted to boolean: {bool_val} (type: {type(bool_val)})\n")
