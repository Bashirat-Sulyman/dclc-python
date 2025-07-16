def divideFive(numbers):
    print("Given List:", GivenList)
    print("Divisible by 5:",)
    for i in numbers:
        if i % 5 == 0:
            print(i)
GivenList = [10, 20, 33, 46, 55]
divideFive(GivenList)