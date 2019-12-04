def integer_division(dividend: int, divisor: int) -> int:
    return dividend // divisor


def float_division(dividend: int, divisor: int) -> float:
    return dividend / divisor


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(integer_division(a, b))
    print(float_division(a, b))
