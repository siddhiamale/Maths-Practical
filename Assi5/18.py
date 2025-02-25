# For Loop :

# 3. Write a program to print the factorial of a given number using a for loop.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}.")
 