from re import sub


def is_isogram(string: str) -> bool:
    string = sub('[ -]', '', string).lower()
    return [0 for letter, index in zip(string, range(len(string))) if letter in string[index + 1:]] == []
