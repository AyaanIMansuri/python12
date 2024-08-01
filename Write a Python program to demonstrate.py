# Write a Python program to demonstrate the use of keyword argument.

def greet(name, greeting="Hello", punctuation="!"):
    """
    Function to print a greeting message.

    Parameters:
    name (str): Name of the person to greet.
    greeting (str): The greeting word. Default is "Hello".
    punctuation (str): The punctuation mark to end the greeting. Default is "!".
    """
    message = f"{greeting}, {name}{punctuation}"
    print(message)

# Example usage of the greet function

# Using only the mandatory argument
greet("Ayaan")

# Using one keyword argument
greet("Mehdi Ali", greeting="Hi")

# Using all arguments as keyword arguments
greet(name="Man patel", greeting="Hey", punctuation="?")

# Mixing positional and keyword arguments
greet("Aman Kazi", punctuation=".")

