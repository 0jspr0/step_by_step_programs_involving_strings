def no_spaces_in_starting_text(text):
    starting_spaces = 0
    while starting_spaces < len(text) and text[starting_spaces] == " ":
        starting_spaces += 1