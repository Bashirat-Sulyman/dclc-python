print("Printing current and previous number and their sum in a range(10)")
previous_number = 0
for current_number in range(10):
    sum = current_number + previous_number
    print("Current Number:", current_number, "    Previous Number:", previous_number, "    Sum:", sum)
    previous_number = current_number