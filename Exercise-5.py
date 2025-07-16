def getTrue(numbers):
   first_element = numbers[0]
   second_element = numbers[-1]
   if first_element == second_element:
    return (True)
   else:
    return (False)
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(getTrue(numbers_x))
print(getTrue(numbers_y))