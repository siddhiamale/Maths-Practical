# Write a python function to check wheter number is perfect or not
def is_perfect(number):
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    return sum_divisors == number

number = 34
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
