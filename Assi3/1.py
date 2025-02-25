# ---write a python program to create fibonacci series upto n using lambda
# write a python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and print the result

# Lambda function to add 15 to a given number
add_15 = lambda x: x + 15

# Lambda function to multiply two arguments
multiply = lambda x, y: x * y

# Test the functions
print("Adding 15 to 20:", add_15(20))
print("Multiplying 20 and 5:", multiply(20, 5))
