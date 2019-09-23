# Score categories.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
REPETITIONS = None


def YACHT(_) -> int:
    most_common = REPETITIONS.most_common(1)[0][1]
    return 50 if most_common == 5 else 0


def FULL_HOUSE(dice: list) -> int:
    most_common = REPETITIONS.most_common(2)
    if most_common[0][1] == 3 and most_common[1][1] == 2:
        return sum(dice)


def FOUR_OF_A_KIND(_) -> int:
    print(REPETITIONS)
    print(REPETITIONS.most_common(1)[0][1])
    most_common = REPETITIONS.most_common(1)[0][1]
    if most_common > 3:
        return 12 if most_common > 4 else 24


def LITTLE_STRAIGHT(_) -> int:
    if set(range(1, 6)) - REPETITIONS.keys() == set():
        return 30


def BIG_STRAIGHT(_) -> int:
    if set(range(2, 7)) - REPETITIONS.keys() == set():
        return 30


def CHOICE(dice: list) -> int:
    return sum(dice)


def score(dice: list, category) -> int:
    global REPETITIONS
    import collections
    REPETITIONS = collections.Counter(dice)

    if isinstance(category, int) and category in range(1, 7):
        return category * REPETITIONS[category]

    result = category(dice)
    if result is None:
        result = 0
    return result
