# While Loop :

# 3. Write a program to print the multiplication table of a given number using
#    a while loop.

num = int(input("Enter number of which you want multiplication table to be printed : "))
i = 1
prod = 1

while i <= 10:
    print (f"{i} * {num} = {i * num}")
    i += 1
