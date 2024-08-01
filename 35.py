def calculate_area(length, width):
    return length * width

# Input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area
area = calculate_area(length, width)

# Display the result
print(f"The area of the rectangle is: {area}")
