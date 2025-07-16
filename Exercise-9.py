def getPalindrome():
    original_num = int(input("Type number: "))
    num_str = str(original_num)
    if num_str == num_str[::-1]:
        print("Yes, given number is palindrome number")
    else:
        print("No, given number is not a palindrome number")
getPalindrome()