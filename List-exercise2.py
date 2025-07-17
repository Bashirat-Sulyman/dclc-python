list1 = [54, 44, 27, 79, 91, 41]
index4 = list1.pop(4)
print("List after removing element at index 4", list1)
list1.insert(2, index4)
print("List after adding element at index 2", list1)
list1.append(index4)
print("List after adding element at last", list1)