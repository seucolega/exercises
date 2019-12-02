RATIO = 2
SQUARES = 64


def square(number: int) -> int:
    if 0 < number < SQUARES + 1:
        return RATIO ** (number - 1)
    raise ValueError("A very specific bad thing happened.")


def total():
    """
    Iterating between all squares works, but uses more resources
    """
    # return sum([square(s + 1) for s in range(n)])

    """
    In order to improve performance, we can apply the formula for the sum of the series in a Geometric Progression.
    Source: https://en.wikipedia.org/wiki/Geometric_progression
    """
    return int((square(1) * (1 - RATIO ** SQUARES)) / (1 - RATIO)) - 1
