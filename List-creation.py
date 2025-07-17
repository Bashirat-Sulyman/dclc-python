given_list1 = [3, 6, 9, 12, 15, 18, 21]
given_list2 = [4, 8, 12, 16, 20, 24, 28]
odd_index = given_list1[1::2]
even_index = given_list2[::2]
combined = odd_index + even_index
print("Element at odd-index positions from list one:", odd_index)
print("Element at even-index positions from list one:", even_index)
print("Printing Final third list:", combined)