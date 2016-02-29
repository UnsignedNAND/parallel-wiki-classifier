def _lower_string(text):
    return text.lower()


def _remove_special_chars(text):
    special_chars = ". , : ; ( ) [ ] < > ? / \\ \" * $ = + - _ { } ! @ # % ^ & \n ! ' |"
    for char in special_chars.split():
        text.replace(char, " ")
    return text


def _trim_white_spaces(text):
    return " ".join(text.split())


def _bag_of_words(text):
    bow = {}
    for word in text.split():
        if word in bow.keys():
            bow[word] += 1
        else:
            bow[word] = 1
    return bow


def simplify(text):
    text = _lower_string(text)
    text = _remove_special_chars(text)
    text = _trim_white_spaces(text)
    return text
