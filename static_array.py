# Course: CS261 - Data Structures

class StaticArrayException(Exception):
    pass

class StaticArray:
    def __init__(self, size=10):
        if size < 1:
            raise StaticArrayException('Array size must be a positive integer')
        self._size = size
        self._data = [None] * size

    def get(self, index: int): ...
    def set(self, index: int, value: object) -> None: ...
    def __getitem__(self, index): ...
    def __setitem__(self, index, value) -> None: ...
    def length(self) -> int: ...