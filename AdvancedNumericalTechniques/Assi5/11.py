# Nested If Statement

# 2. Write a program to check if a person is eligible to donate blood
#    (age >= 18 and weight >= 50 kg).

age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood due to weight.")
else:
    print("You are not eligible to donate blood due to age.")