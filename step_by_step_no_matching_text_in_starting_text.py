def no_matching_text_in_starting_text(text, text_to_remove):
    if text.startswith(text_to_remove):
        return text[len(text_to_remove):]
    return text