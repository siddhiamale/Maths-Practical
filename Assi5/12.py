# Nested If Statement
# 3. Write a program to check if a student is eligible for a scholarship
#      (GPA >= 3.5 and family income <= $50,000).

gpa = float(input("Enter your GPA: "))
income = int(input("Enter you family income: "))

if gpa >= 3.5:
    if income <= 50000:
        print("You are eligible for scholarship..")
    else:
        print("You are not eligible for scholarship..")
else:
    print("GPA must be grater than 3.5")