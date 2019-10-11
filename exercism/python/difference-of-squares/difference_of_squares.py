def first_n_natural_numbers(number: int) -> list:
    return list(range(1, number + 1))


def square_of_sum(number: int) -> int:
    return sum(first_n_natural_numbers(number)) ** 2


def sum_of_squares(number: int) -> int:
    numbers = first_n_natural_numbers(number)
    return sum([number ** 2 for number in numbers])


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)
