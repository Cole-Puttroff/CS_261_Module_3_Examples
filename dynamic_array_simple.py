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
        return self.data[index]


    def append(self, val):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        # Removed the else — now the append always runs after resizing if needed
        self.data[self.size] = val
        self.size += 1


    def resize(self, new_capacity: int) -> None:
        new_array = StaticArray(new_capacity)

        for k in range(self.size):
            new_array[k] = self.data[k]

        self.data = new_array  # Point to the new array
        self.capacity = new_capacity


# Create new instance of Dynamic_Array
my_list = Dynamic_Array()

# Build list with 10 items
for k in range(12):
    my_list.append(k)

# Output list
for k in range(0, my_list.size):
    print(my_list[k])