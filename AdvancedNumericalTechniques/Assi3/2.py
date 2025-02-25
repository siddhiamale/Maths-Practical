# write python program to create a function that takes one argument,and that argument will be multiplied with an unknown given number

def multiplier(fixed_number):
    return lambda x: x * fixed_number

# Create a multiplier with the unknown number (e.g., 7)
multiply_by_7 = multiplier(7)

# Test the function
print("5 multiplied by 7:", multiply_by_7(5))
print("10 multiplied by 7:", multiply_by_7(10))
 