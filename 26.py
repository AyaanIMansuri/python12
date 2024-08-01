def sum_of_first_n_odd_numbers(n):
    sum_odd_numbers = 0
    current_odd_number = 1

    for _ in range(n):
        sum_odd_numbers += current_odd_number
        current_odd_number += 2  # Move to the next odd number

    return sum_odd_numbers

# Calculate the sum of the first 20 odd numbers
n = 20
sum_odd = sum_of_first_n_odd_numbers(n)
print(f"The sum of the first {n} odd numbers is {sum_odd}.")
