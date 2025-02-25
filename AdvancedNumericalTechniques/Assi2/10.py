# Write a python function that checks whether passed string is palindrome or not
def palindrome(str):
    newStr=str[::-1]
    if(str == newStr):
        print(f"passed string {str} is palindrome")
    else:
        print(f"passed string {str} is not palindrome")

palindrome("nayan")
