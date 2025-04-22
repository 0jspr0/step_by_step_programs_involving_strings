def spaces_6_digit_format(number):
    if len(number) >= 6:
        return number
    number_of_zeros = 6 - len(number)
    return "0" * number_of_zeros + number

number = input("Enter a number: ")
result = spaces_6_digit_format(number)