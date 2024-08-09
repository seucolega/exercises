RATIO = 2
SQUARES = 64


def square(number: int) -> int:
    if 0 < number <= SQUARES:
        return RATIO ** (number - 1);

    raise ValueError("A very specific bad thing happened.")


def total():
    return square(SQUARES) * RATIO - 1;
