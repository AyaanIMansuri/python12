# Python program to demonstrate different string methods

# Define a sample string
sample_string = "Hello, World!"

# Demonstrating string methods
print("Original String: ", sample_string)

# Convert to uppercase
upper_case = sample_string.upper()
print("Uppercase: ", upper_case)

# Convert to lowercase
lower_case = sample_string.lower()
print("Lowercase: ", lower_case)

# Swap case
swap_case = sample_string.swapcase()
print("Swap Case: ", swap_case)

# Capitalize the first letter
capitalized = sample_string.capitalize()
print("Capitalized: ", capitalized)

# Title case
title_case = sample_string.title()
print("Title Case: ", title_case)

# Find the position of a substring
substring = "World"
position = sample_string.find(substring)
print(f"Position of '{substring}': ", position)

# Check if string starts with a specific substring
starts_with = sample_string.startswith("Hello")
print("Starts with 'Hello': ", starts_with)

# Check if string ends with a specific substring
ends_with = sample_string.endswith("World!")
print("Ends with 'World!': ", ends_with)

# Replace a substring
replaced_string = sample_string.replace("World", "Universe")
print("Replaced String: ", replaced_string)

# Split the string into a list
split_string = sample_string.split(", ")
print("Split String: ", split_string)

# Join a list into a string
joined_string = ", ".join(split_string)
print("Joined String: ", joined_string)

# Strip whitespace
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print("Stripped String: '", stripped_string, "'", sep="")

# Check if all characters are alphabetic
is_alpha = sample_string.isalpha()
print("Is Alphabetic: ", is_alpha)

# Check if all characters are digits
is_digit = "12345".isdigit()
print("Is Digit: ", is_digit)

# Check if all characters are alphanumeric
is_alnum = "Hello123".isalnum()
print("Is Alphanumeric: ", is_alnum)
