"""
Guido's Gorgeous Lasagna on Exercism's Python Track
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Calculate preparation time in minutes

    :param layers: int
    :return: int
    """
    return 2 * layers


def elapsed_time_in_minutes(layers: int, time: int):
    """Calculate total elapsed cooking time (prep + bake) in minutes

    :param layers: int
    :param time: int
    :return: int
    """
    return preparation_time_in_minutes(layers) + time
