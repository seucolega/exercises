def if_else(n: int) -> str:
    if n % 2 or 6 <= n <= 20:
        return 'Weird'
    else:
        if 2 <= n <= 5 or n > 21:
            return 'Not Weird'
