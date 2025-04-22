def spaces_6_digit_format(number):
    if len(number) >= 6:
        return number
    number_of_zeros = 6 - len(number)