def matching_starting_text_checker(text, starting_text):
    if len(starting_text) > len(text):
        return False
    return text[:len(starting_text)] == starting_text

text = input("Enter text: ")
starting_text = input("Enter starting text: ")
result = matching_starting_text_checker(text, starting_text)