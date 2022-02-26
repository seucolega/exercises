from re import sub


def is_isogram(string: str) -> bool:
    string = sub('[ -]', '', string).lower()

    for index in range(len(string)):
        if string[index] in string[index + 1:]:
            return False

    return True
