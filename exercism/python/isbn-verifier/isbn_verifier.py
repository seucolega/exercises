from re import search


def is_valid(isbn: str) -> bool:
    match = search(r'^(\d{9})(\d|X)$', isbn.replace('-', ''))
    if not match:
        return False
    isbn = list(match.string)
    return sum([10 if digit == 'X' else int(digit) * index for digit, index in zip(isbn, range(10, 0, -1))]) % 11 == 0
