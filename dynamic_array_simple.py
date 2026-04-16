from static_array import StaticArray

class Dynamic_Array:
    def __init__(self, start_array=None):
        self.size = 0
        self.capacity = 10
        self.data = StaticArray(self.capacity)

        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self):
        return str(self.data)

    def __getitem__(self, index):
        ...

    # Will need to be amended to check if there is room and call function to expand array when necessary
    def append(self, val):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        else:
            self.data[self.size] = val
            self.size = self.size + 1

    # Add a function that will create an expanded array with twice the size with the same elements
    def resize(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        """
        new_array = StaticArray(new_capacity)

        for k in range(0, self.size):
            new_array[k] = self.data[k]


if __name__ == "__main__":
    # Create new instance of Dynamic_Array
    my_list = Dynamic_Array()

    # Build list with 10 items
    for i in range(10):
        my_list.append(i)

    # Output list
    for i in range(0, my_list.size):
        print(my_list[i])