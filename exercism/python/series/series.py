def slices(series: str, length: int) -> list:
    if 0 < length <= len(series):
        return [series[index:index + length] for index in range(0, len(series) - length + 1)]
    else:
        raise ValueError('A very specific bad thing happened.')