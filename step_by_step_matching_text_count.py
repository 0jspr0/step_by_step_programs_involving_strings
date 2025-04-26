def matching_text_count(text, text_to_count):
    text_count = 0
    index = 0
    while True:
        index = text.find(text_to_count, index)
        if index == -1:
            break