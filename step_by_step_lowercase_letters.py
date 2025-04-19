def lowercase_letters(text):
    result = ""
    for i in text:
        if "A" <= i <= "Z":
            result += chr(ord(i) + 32)
        else:
            result += i
    return result

text = input("Enter text: ")