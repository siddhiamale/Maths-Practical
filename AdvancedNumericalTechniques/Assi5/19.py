# Nested Loops :

# 1. Write a program to print the multiplication table of numbers from
#     1 to 10 using nested loops.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each table