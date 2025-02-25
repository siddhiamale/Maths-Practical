# If-Elif-Else Statement

# 2. Write a program to check the age group of a person
#    (child: 0-12, teenager: 13-19, adult: 20-64, senior: 65+).

age = int(input("Enter your age :"))

if age <=12:
    print("You are a child.")
elif age >=13 and age <= 19:
    print("You are a teenager.")
elif age >=20 and age <= 64:
    print("You are adult")
else:
    print("You are a senior.")