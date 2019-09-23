def compare_the_triplets(a: list, b: list) -> list:
    if 3 == len(a) == len(b):
        result = 2 * [0]
        for i in range(3):
            result[0] += 1 if a[i] > b[i] else 0
            result[1] += 1 if b[i] > a[i] else 0
        return result
    else:
        raise ValueError('A very specific bad thing happened.')
