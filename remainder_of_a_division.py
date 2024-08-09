def remainder_of_a_division(a: int, b: int):
    if b > a:
        return a
    else:
        return remainder_of_a_division(a - b, b)


print(remainder_of_a_division(5, 2))

