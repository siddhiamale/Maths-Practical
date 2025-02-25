# While Loop

# 3. Write a program to print the exponentiation table of numbers from 1 to 10
#     using a while loop. 1 ^ 1 = 1,1 ^ 2 = 1,1 ^ 3 = 1...2 ^ 1 = 2,2 ^ 2 = 4,2 ^ 3 = 8...

i = 1
while i <= 10:
    j=1
    while j <= 10:
        print(f"{i} ^ {j} = {i ** j}")
        j += 1
    i += 1
    print()