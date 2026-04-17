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

    def __getitem__(self, index):
        return self._data[index]


    def append(self, val):
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        # Removed the else — now the append always runs after resizing if needed
        self._data[self._size] = val
        self._size += 1


    def resize(self, new_capacity: int) -> None:
        new_array = StaticArray(new_capacity)

        for k in range(self._size):
            new_array[k] = self._data[k]

        self._data = new_array  # Point to the new array
        self._capacity = new_capacity

    def length(self) -> int:
        return self._size


my_list = Dynamic_Array()

# Build list with 10 items
for k in range(20):
    my_list.append(k)

my_list.__iter__()

# Output list
for k in range(0, my_list.length()):
    print(my_list.__next__())

