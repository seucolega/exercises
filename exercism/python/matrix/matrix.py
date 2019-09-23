class Matrix(object):
    def __init__(self, matrix_string: str):
        self._data = [[int(col) for col in row.split()] for row in matrix_string.splitlines()]

    def row(self, index: int) -> [int]:
        return self._data[index - 1][:]

    def column(self, index: int) -> [int]:
        return [row[index - 1] for row in self._data]
