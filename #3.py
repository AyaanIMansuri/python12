# WAP AREA OF CUBOID

# L B H 
import os

# Clearing the Screen
os.system('cls')
L = int(input("Enter lenght\n"))

B = int(input("Enter breadth\n"))

H = int(input("Enter height\n"))


A = 2 * (L * B + B * H + H * 1)

print("The Area is\n",A)