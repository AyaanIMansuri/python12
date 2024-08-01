# Function to calculate the sum of all digits of a given number
def sum_of_digits(number):
    # Ensure the number is positive
    number = abs(number)
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    return total_sum

# Get user input
try:
    user_input = int(input("Enter a number: "))
    result = sum_of_digits(user_input)
    print(f"The sum of all digits of {user_input} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
