def no_matching_text_in_starting_text(text, text_to_remove):
    if text.startswith(text_to_remove):
        return text[len(text_to_remove):]
    return text

text = input("Enter text: ")
text_to_remove = input("Enter text to remove: ")
result = no_matching_text_in_starting_text(text, text_to_remove)
print(result)