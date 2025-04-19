def all_letters_uppercase_checker(text):
    for i in text:
        if "a" <= i <= "z":
            return False
    return True

text = input("Enter text: ")