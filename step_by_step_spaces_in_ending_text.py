def spaces_in_ending_text(text, number_of_spaces):
    if len(text) >= number_of_spaces:
        return text
    number_of_spaces -= len(text)
    return text + " " * number_of_spaces

text = input("Enter text: ")