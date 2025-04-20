def matching_ending_text_checker(text, ending_text):
    if len(ending_text) > len(text):
        return False
    return text[-len(ending_text):] == ending_text

text = input("Enter text: ")
ending_text = input("Enter ending text: ")
result = matching_ending_text_checker(text, ending_text)