def no_spaces_in_ending_text(text):
    ending_spaces = len(text) - 1
    while ending_spaces >= 0 and text[ending_spaces] == " ":
        ending_spaces -= 1
    return text[:ending_spaces + 1]

text = input("Enter text: ")
result = no_spaces_in_ending_text(text)
print(result)