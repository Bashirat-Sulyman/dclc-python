def get_even():
    original_string= input("Type a word ")
    even_letter= original_string[::2]
    for i in even_letter:
        print(i)
get_even()