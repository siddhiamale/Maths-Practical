# Write a python program that accepts hyphen-separated sequence of words as input and prints words in hyphen-separated sequence after sorting them 
#   alphabetically
words="red-black-green-orange"
new="-".join(sorted(words.split('-')))
print(new)