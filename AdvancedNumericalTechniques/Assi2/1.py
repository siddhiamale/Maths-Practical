# Write a python function to find maximum of 3 numbers
def max(a,b,c):
    if(a > b and a > c):
        print(f"maximum of 3 numbers is : {a}")
    elif(b > a and b > c):
        print(f"maximum of 3 numbers is : {b}")
    else:
        print(f"maximum of 3 numbers is : {c}")

max(10,3,6)