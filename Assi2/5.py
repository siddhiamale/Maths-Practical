# Write a python function to calculate factorial of number.(function accept number as an argument)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(f"Factorial of given numbers {fact(5)}")

