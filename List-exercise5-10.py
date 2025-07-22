# List Exercise 5
# Creating a python set
first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List", first_list)
second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List", second_list)
result = zip(first_list, second_list)
print("Result is",list(result))

#List Exercise 6
# Finds intersection (common items)
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
common_items = first_set.intersection(second_set)
print("Intersection is", common_items)

#removes common items
for item in common_items:
    first_set.remove(item)
print("First Set after removing common element ", first_set)


#List Exercise 7
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

#checks for subset and superset
print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of first set -", second_set.issubset(first_set))

print("First set is Super set of Second set -", first_set.issuperset(second_set))
print("Second set is Super set of First set -", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

#List Exercise 8
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print("List: ", roll_number)
print("Dictionary: ", sample_dict)

for item in roll_number:
    if item in sample_dict.values():
        print(item)

filtered = [item for item in roll_number if item in sample_dict.values()]
print("After removing unwanted elements from list ", filtered)

# List Exercise 9
#Removing duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
print("Dictionary Values: ", speed.values())
List = list(speed.values())

NewList = []
for value in List:
    if value not in NewList:
        NewList.append(value)
print("Unique List:", NewList)


# Exercise 10

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Given List: ", sample_list)

# Checks Duplicates
unique_list = []
for value in sample_list:
    if value not in unique_list:
        unique_list.append(value)
print("Unique List:", unique_list)

# Changes list to tuple
my_tuple = tuple(unique_list)
print("Tuple List:", my_tuple)

# Checks minimum and maximum number from the list
MinNum = min(unique_list)
MaxNum = max(unique_list)
print("Minimum Number is: ", MinNum)
print("Maximum Number is: ", MaxNum)