# Python program to demonstrate formatted strings

# Using % formatting
name = "Alice"
age = 30
height = 5.5
formatted_string_percent = "Name: %s, Age: %d, Height: %.1f" % (name, age, height)
print("Using % formatting: ", formatted_string_percent)

# Using str.format()
formatted_string_format = "Name: {}, Age: {}, Height: {:.1f}".format(name, age, height)
print("Using str.format(): ", formatted_string_format)

# Using str.format() with positional arguments
formatted_string_positional = "Name: {0}, Age: {1}, Height: {2:.1f}".format(name, age, height)
print("Using str.format() with positional arguments: ", formatted_string_positional)

# Using str.format() with named placeholders
formatted_string_named = "Name: {n}, Age: {a}, Height: {h:.1f}".format(n=name, a=age, h=height)
print("Using str.format() with named placeholders: ", formatted_string_named)

# Using f-strings (formatted string literals)
formatted_string_fstring = f"Name: {name}, Age: {age}, Height: {height:.1f}"
print("Using f-strings: ", formatted_string_fstring)

# Aligning text
left_aligned = f"{name:<10} | {age:<5} | {height:<5.1f}"
center_aligned = f"{name:^10} | {age:^5} | {height:^5.1f}"
right_aligned = f"{name:>10} | {age:>5} | {height:>5.1f}"
print("Left aligned:   ", left_aligned)
print("Center aligned: ", center_aligned)
print("Right aligned:  ", right_aligned)

# Using f-strings with expressions
expression_demo = f"{name} will be {age + 1} next year."
print("Using f-strings with expressions: ", expression_demo)

# Formatting numbers
large_number = 1234567890
formatted_number = f"{large_number:,}"
print("Formatted number with commas: ", formatted_number)

# Formatting percentages
percentage = 0.853
formatted_percentage = f"{percentage:.2%}"
print("Formatted percentage: ", formatted_percentage)
