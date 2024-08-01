# Function to check if a digit is even or odd
def check_even_odd(digit):
    # Check if the digit is between 0 and 9
    if digit < 0 or digit > 100:
        return "Input is not a  digit."
    
    # Determine if the digit is even or odd
    if digit % 2 == 0:
        return "The digit is even."
    else:
        return "The digit is odd."

# Get user input
try:
    user_input = int(input("Enter a digit: "))
    result = check_even_odd(user_input)
    print(result)
except ValueError:
    print("Invalid input. Please enter a  digit.")
