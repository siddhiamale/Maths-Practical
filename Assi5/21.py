# While Loop

# 1. Write a program to print the multiplication table of 5 using a while loop.
#    5 x 1 = 5 ,5 x 2 = 10 ,5 x 3 = 15...5 x 10 = 50

num = 5
i = 1

while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1