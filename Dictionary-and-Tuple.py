# DICTIONARY
# Exercise 1 Perform basic dictionary operations

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print('Original dictionary:', my_dict)

# Add a key value
my_dict['profession'] = 'Doctor'
print("Updated dictionary after adding 'profession':", my_dict)

# Modify a key value
my_dict['age'] = 40
print("Updated dictionary after modification:", my_dict)

# Prints a key value
print("City:", my_dict['city'])

# Exercise 2
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print("Original dictionary:", my_dict)
del my_dict ['profession']
print(f"Updated dictionary after removing 'profession':", my_dict)

# Print key values
for key, value in my_dict.items():
    print(f"{key} : {value}")

# Check if Key exists
def checkKey (dictionary, key_to_check):
    return key_to_check in dictionary

key1 = 'age'
print(f"Does '{key1}' exist? {checkKey(my_dict, key1)}")

# Dictionary form Lists
keys =['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print("First List:", keys)
print("Second List:", values)
zipped = dict(zip(keys, values))
print("List converted to dictionary:", zipped)

# Clear Dictionary
my_dict ={'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict.clear()
print("Dictionary after removing all item", my_dict)

# Merge Two dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print("First Dictionary", dict1)
print("Second Dictionary", dict2)
dict1.update(dict2)
print("Merged List:", dict1)

# Count Character Frequencies
string1 = 'Jessa'
freq = {}
for char in string1:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] =1
print("Frequencies for Jessa", freq)

# Access Nested Dictionary
nested_dict = {'person': {'name': 'Alice', 'age': 30}}
print(f'Nested Dictionary: {nested_dict}')
# Get the key value age
aliceAge = nested_dict['person'] ['age']
print(f'Alice age is: {aliceAge}')

# Print the value of key ‘history’ from nested dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(f'Given Dictionary: {sampleDict}')
print(sampleDict['class'] ['student'] ['marks'] ['history'])

#OR
historyValue = sampleDict['class']['student'] ['marks'] ['history']
print(historyValue)

# Modify Nested Dictionary
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(f'Original Dictionary {nested_student_dict}')
nested_student_dict['class'] ['student'] ['name'] = "Jessa"
print(f'Modified Dictionary: {nested_student_dict}')

# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
my_dict = dict.fromkeys(employees, defaults)
print(my_dict)

# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
newDict = {}
for key in keys:
    if key in sample_dict:
        newDict[key] = sample_dict[key]
print(f'New Dictionary: {newDict}')

# Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for key in keys:
    if key in sample_dict:
        sample_dict.pop(key)
print(f'New Dictionary: {sample_dict}')

# Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
for value in sample_dict.values():
    print(value)
if 200 in sample_dict.values():
    print(f'200 is present in given dictionary')

# Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['Location']= sample_dict.pop('city')
print(sample_dict)

# Get the key of a minimum value
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min_key = min(sample_dict, key=sample_dict.get)
min_value = sample_dict[min_key]
print(min_key, min_value)

# Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3'] ['salary'] = 8500
print(sample_dict)

# Invert Dictionary
original_dict1 = {'a': 1, 'b': 2, 'c': 3}
print(f'Original Dictionary: {original_dict1}')
inverted = {}
for key, value in original_dict1.items():
    inverted[value] = key
print(f'Inverted Dictionary: {inverted}')

# Sort Dictionary by Keys
my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
print(f'Original Dictionary: {my_dict}')
OrderedList = dict(sorted(my_dict.items()))
print(f'Sorted by keys (as OrderedDict): {OrderedList}')

# Sort Dictionary by Values
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print(f'Original Dictionar: {my_dict}')
sorted_list = dict(sorted(my_dict.items(), key =lambda item: item [1]))
print(f'Sorted List: {sorted_list}')

#TUPLE
# Creating a tuple
my_tuple = (1,2,3,4)
print(my_tuple)

# Tuple Repetition
original_tuple = ('a', 'b')
Repeated_tuple = original_tuple *3
print(f'Reapeated Tuple: {Repeated_tuple}')

# Slicing Tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slice_num = numbers[3:7]
print("Sliced Number from the 4th to the 7th position:", slice_num)

# Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
reversed_tuple = tuple1[::-1]
print(f'Reversed Tuple: {reversed_tuple}')

# Access Nested Tuples
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
nested_tuples = tuple1[1][1]
print(nested_tuples)

#Create a tuple with single item 50
t1 = (50,)
print(t1)

# Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
a,b,c,d = tuple1
print(a)
print(b)
print(c)
print(d)

# Swap two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)

print('Before swap:')
print('tuple1 =', tuple1)
print('tuple2 =', tuple2)

# Swap
tuple1, tuple2 = tuple2, tuple1

print('After Swap:')
print('tuple2 =', tuple2)
print('tuple1 =', tuple1)

# Copy Specific Elements From Tuple
tuple1 = (11, 22, 33, 44, 55, 66)
print("Tuple1:", tuple1)
tuple2 = tuple1[3:5]
print("Tuple2:", tuple2)

# List to Tuple
my_list = [10, 20, 30]
tuple_list = tuple(my_list)
print(f'Converted list to tuple: {tuple_list}')

# Function Returning Tuple
def get_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return (min_value, max_value)

my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")

# Comparing Tuples
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(f'Tuple 1: {t1}')
print(f'Tuple 2: {t2}')

if t1>t2:
    print(f'{t1} is greater than {t2}')
elif t1<t2:
    print(f'{t1} is less than {t2}')
else:
    print(f'{t1} is equal to {t2}')

# Removing Duplicates from Tuple
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f'Tuple with duplicates: {my_tuple}')
remove_duplicate = tuple(set(my_tuple))
print(f'Tuple after removing duplicates: {remove_duplicate}')

# Filter Tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print(f'Original List: {students}')

Top_scorer = []
for student in students:
    if student[1] >= 90:
        Top_scorer.append(student)
print(Top_scorer)