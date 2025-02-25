# Write a python function that takes a list and returns new list , which distinct elements from first list


def get_elements(input_list):   # set :- removes duplicates because sets do not allow duplicate elements.
    return list(set(input_list))         # list :- converts the set back into a list to get the desired format.

list1 = [1, 2, 3, 3, 3, 4, 4, 5, 5]
print(f"New string {get_elements(list1)}")