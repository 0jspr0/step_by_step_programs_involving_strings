def no_matching_text_in_ending_text(text, text_to_remove):
    if text.endswith(text_to_remove):
        return text[:-len(text_to_remove)]
    return text