from static_array import StaticArray


class DynamicArrayException(Exception):
    pass


class Dynamic_Array_Iterator:
    def __init__(self, dyn_array):
        self._index = 0
        self._dyn_array = dyn_array

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._dyn_array.length():
            raise StopIteration
        value = self._dyn_array.get_at_index(self._index)
        self._index = self._index + 1
        return value

    def next(self):
        return self.__next__()


class Dynamic_Array:
    def __init__(self, start_array=None):
        self._size = 0
        self._capacity = 10
        self._data = StaticArray(self._capacity)

        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __iter__(self):
        return Dynamic_Array_Iterator(self)

    def __str__(self):
        return str(self._data)

    def append(self, val):
        # Will need to be amended to check if there is room
        # and call method to expand array when necessary
        if self._size == self._capacity:
            self.resize(self._capacity*2)
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

    def get_at_index(self, index: int) -> object:
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def length(self) -> int:
        return self._size
