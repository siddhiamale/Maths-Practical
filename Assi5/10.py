# Nested If Statement

# 1. Write a program to check if a number is a perfect square and
#      also greater than 100.

num = int(input("Enter a number:"))
if num > 100:
    if (num ** 0.5) % 1 == 0:
        print("The number is a perfect square and greater than 100.")
    else:
        print("The number is not a perfect square and greater than 100.")
else:
    print("The number is not greater than 100.")