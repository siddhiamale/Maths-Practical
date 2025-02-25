# Write a python function to create and print a list where the values are the squares of numbers between 1 to 30 (both included)

def square_list():
    squares=[]
    for i in range(1,31):
        squares.append(i**2)
    print(squares)


square_list()