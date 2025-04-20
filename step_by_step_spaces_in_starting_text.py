def spaces_in_starting_text(text, number_of_spaces):
    if len(text) >= number_of_spaces:
        return text
    number_of_spaces -= len(text)
    return " " * number_of_spaces + text