# write a python program to detect the number of local variables declared in a function 

def my_function():
    a = 10
    b = 20
    c = a + b

print(my_function.__code__.co_nlocals)  # Prints the number of local variables
