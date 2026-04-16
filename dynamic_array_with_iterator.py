from static_array import StaticArray, StaticArrayException

class DynamicArrayException(Exception):
    pass

class Dynamic_Array:
    def __init__(self, start_array=None):
        self._size = 0
        self._capacity = 10
        self._data = StaticArray(self._capacity)
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        try:
            value = self._data[self._index]
        except StaticArrayException:
            raise StopIteration
        self._index = self._index + 1
        return value

    def __str__(self):
        return str(self._data)

    def append(self, val):
        # Will need to be amended to check if there is room
        # and call method to expand array when necessary
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        else:
            self._data[self._size] = val
            self._size = self._size + 1

    def resize(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        """
        new_array = StaticArray(new_capacity)

        for k in range(0, self._size):
            new_array[k] = self._data[k]

        pass
