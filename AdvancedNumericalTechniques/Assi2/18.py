# write a python program to access a function inside a function

def outer_function():
    print("This is the Outer Function...!")

    def inner_function():
        print("This is the Inner Function...!")

    inner_function()

outer_function()