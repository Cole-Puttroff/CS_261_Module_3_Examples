class StaticArray:
    def __init__(self, size=10):
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')
        self._size = size
        self._data = [None] * size

    def get(self, index: int):
        if index < 0 or index >= self._size:
            raise StaticArrayException('Index out of bounds')
        return self._data[index]

    def set(self, index: int, value: object) -> None:
        if index < 0 or index >= self._size:
            raise StaticArrayException('Index out of bounds')
        self._data[index] = value

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value) -> None:
        self.set(index, value)

    def length(self) -> int:
        return self._size

    def __str__(self):
        return str(self._data)