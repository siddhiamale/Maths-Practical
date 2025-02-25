# Nested Loops :

# 2. Write a program to print the pattern of numbers as follows :
#    12 34 5 67 8 9 10using nested loops.Tables using nested loops

k=1
for i in range(1, 5):
    for j in range(1, i+1):
        print( k, end=" ")
        k += 1
    print()  # Print a new line after each table