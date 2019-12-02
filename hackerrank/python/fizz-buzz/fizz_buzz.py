def fizz_buzz(number: int) -> str:
    divider_and_text = (
        (3, 'Fizz'),
        (5, 'Buzz')
    )
    return ''.join([item[1] for item in divider_and_text if number % item[0] == 0]) or str(number)


if __name__ == '__main__':
    for i in range(1, 101):
        print(fizz_buzz(i))
