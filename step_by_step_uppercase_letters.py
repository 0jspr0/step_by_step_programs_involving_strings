def uppercase_letters(text):
    result = ""
    for i in text:
        if "a" <= i <= "z":
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

text = input("Enter text: ")
result = uppercase_letters(text)
print(result)