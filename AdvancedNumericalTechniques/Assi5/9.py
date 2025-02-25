# If-Elif-Else Statement

# 3. Write a program to check the type of a triangle based on the lengths
#     of its sides (equilateral, isosceles, scalene).

side1 = int(input("Enter the length of the first side:"))
side2 = int(input("Enter the length of the second side:"))
side3 = int(input("Enter the length of the third side:"))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")