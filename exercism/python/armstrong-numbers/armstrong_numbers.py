from math import pow


def is_armstrong_number(number: int) -> bool:
    digits = len(str(number))
    return number == sum([pow(int(digit), digits) for digit in str(number)])
