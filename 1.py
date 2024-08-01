def is_leap_year(year):
    # Check if the year is divisible by 4
    import os

    os.system('cls')

    if year % 4 == 0:
        # Check if the year is also divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True  # Divisible by 4, 100, and 400 -> Leap year
            else:
                return False  # Divisible by 4 and 100 but not by 400 -> Not a leap year
        else:
            return True  # Divisible by 4 but not by 100 -> Leap year
    else:
        return False  # Not divisible by 4 -> Not a leap year
    
     
# Input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
