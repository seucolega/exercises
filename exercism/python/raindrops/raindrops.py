def convert(number: int) -> str:
    dictionary = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    return ''.join([text for divider, text in dictionary.items() if number % divider == 0]) or str(number)
