def spaces_in_starting_and_ending_text(text, number_of_spaces):
    if len(text) >= number_of_spaces:
        return text
    number_of_ending_spaces = number_of_spaces // 2
    number_of_starting_spaces = number_of_spaces - number_of_ending_spaces
    return " " * number_of_starting_spaces + text + " " * number_of_ending_spaces

text = input("Enter text: ")
number_of_spaces = int(input("Enter a number of spaces: "))
result = spaces_in_starting_and_ending_text(text, number_of_spaces)
print(result)