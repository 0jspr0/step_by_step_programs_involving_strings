def all_letters_lowercase_checker(text):
    for i in text:
        if "A" <= i <= "Z":
            return False
    return True

text = input("Enter text: ")
result = all_letters_lowercase_checker(text)