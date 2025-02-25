# Write a python function that accepts string and returns no. of uppercase and lowercase letters in string
def countLetters(str):
    upperCount=0
    lowerCount=0
    for char in str:
        if char.isupper():
            upperCount += 1
        elif char.islower():
            lowerCount += 1
    return upperCount,lowerCount
str="I am Siddhi Amale"
uppercase,lowercase=countLetters(str)
print(f"No. of upper case characters {uppercase}")
print(f"No. of lower case characters {lowercase}")
     