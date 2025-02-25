# While Loop

# 2. Write a program to print the addition table of numbers from 1 to 10 using
#      a while loop. 1 + 1 = 2 ,1 + 2 = 3 ,1 + 3 = 4... ,2 + 1 = 3 ,2 + 2 = 4...

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i} + {j} = {i + j}")
        j += 1
    i += 1
    print()  # Print a new line after each table