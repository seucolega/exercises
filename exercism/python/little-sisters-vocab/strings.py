"""Little Sister's Vocabulary exercise"""


def add_prefix_un(word: str) -> str:
    """Add a prefix to a word

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return f'un{word}'


def make_word_groups(vocab_words: list) -> str:
    """Add prefixes to word groups

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.
    """

    prefix = vocab_words[0]
    vocab_words[0] = ''

    return ' :: '.join(f'{prefix}{word}' for word in vocab_words)


def remove_suffix_ness(word: str) -> str:
    """Remove a suffix from a word

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    word = word[:-4]

    return f'{word[:-1]}y' if word.endswith('i') else word


def adjective_to_verb(sentence: str, index: int) -> str:
    """Extract and transform a word

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart. The function should return the extracted
    adjective as a verb.
    """

    words = sentence.rstrip('.').split()

    return f'{words[index]}en'
