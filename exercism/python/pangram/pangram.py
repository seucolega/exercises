from string import ascii_lowercase as alphabet


def is_pangram(sentence: str) -> bool:
    sentence = sentence.lower()
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
