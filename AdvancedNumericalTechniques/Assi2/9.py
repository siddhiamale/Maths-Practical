# Write a python program to print even numbers from given list
list1=[1,2,3,4,5,6,7,8,9]
newList=[]
for i in list1:
    if i % 2 == 0:
        newList.append(i)

print(newList)