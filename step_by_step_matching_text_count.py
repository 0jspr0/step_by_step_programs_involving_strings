def matching_text_count(text, text_to_count):
    text_count = 0
    index = 0
    while True:
        index = text.find(text_to_count, index)
        if index == -1:
            break
        text_count += 1
        index += len(text_to_count)
    return text_count

text = input("Enter text: ")
text_to_count = input("Enter text to count: ")
result = matching_text_count(text, text_to_count)
print(result)