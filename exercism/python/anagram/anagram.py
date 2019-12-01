def break_word_in_letters(word: str) -> [str]:
    return list(word.lower())


def is_anagram(word: [str], candidate: [str]) -> bool:
    return word != candidate and sorted(word) == sorted(candidate)


def find_anagrams(word: str, candidates: [str]) -> list:
    word = break_word_in_letters(word)
    return [candidate for candidate in candidates if is_anagram(word, break_word_in_letters(candidate))]
