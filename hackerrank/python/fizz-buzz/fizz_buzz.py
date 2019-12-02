DIVIDER_AND_TEXT = (
    (3, 'Fizz'),
    (5, 'Buzz')
)


def fizz_buzz(number: int) -> str:
    return ''.join([item[1] for item in DIVIDER_AND_TEXT if number % item[0] == 0]) or str(number)


if __name__ == '__main__':
    for i in range(1, 101):
        print(fizz_buzz(i))
