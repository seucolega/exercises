def slices(series: str, length: int) -> list:
    if not series:
        raise ValueError('series cannot be empty')

    if length < 1:
        if length == 0:
            raise ValueError('slice length cannot be zero')
        raise ValueError('slice length cannot be negative')

    slices = len(series) - length + 1
    
    if slices < 1:
        raise ValueError('slice length cannot be greater than series length')

    return [series[index:index + length] for index in range(slices)]