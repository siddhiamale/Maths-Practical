# Write a python function to multiply all numbers in list
def multiply(numbers):
    result=1
    for num in numbers:
        result *= num
    return result
numbers=[8,2,3,-1,7]
print(f"Multiplication of all numbers in list {multiply(numbers)}")