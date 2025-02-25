# Write a python function to check whether a string is a pangram or not 
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())            


sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")



""" --s.lower() converts the input string s to lowercase. This step ensures the function is case-insensitive. 
    --set('abcdefghijklmnopqrstuvwxyz') creates a set containing all the lowercase English letters from 'a' to 'z'. A set is a collection of unique elements, so even 
        if a letter appears multiple times in the string, it will only be counted once.
    --set(s.lower()) converts the lowercase version of the input string s into a set of characters. This will remove any duplicate letters from the string,
        leaving only unique characters that are alphabetic.
    --The <= operator is used to check if one set is a subset of another. In this case, it checks if the set of all 26 letters (set('abcdefghijklmnopqrstuvwxyz')) 
        is a subset of the set of characters in the string (set(s.lower())).

    """