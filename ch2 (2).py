# Function to calculate the sum of numbers divisible by both 3 and 5 up to a given limit
def sum_divisible_by_3_and_5(limit):
    total_sum = 0
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            total_sum += number
    return total_sum

# Define the limit
limit = 100

# Calculate the sum
result = sum_divisible_by_3_and_5(limit)

# Print the result
print(f"The sum of all numbers up to {limit} that are divisible by both 3 and 5 is:\n{result}")
