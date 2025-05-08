import numpy as np
from time import time

# Custom implementation of a dynamic array list using numpy
class ArrayList:
    def __init__(self):
        # Initial capacity and size
        self.capacity = 10
        self.size = 0
        # Initialize the array with a fixed capacity using numpy
        self.array = np.empty(self.capacity, dtype=object)

    # Enable iteration over the ArrayList
    def __iter__(self):
        return ArrayListIterator(self.array, self.size)

    # Get element at index i
    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        return self.array[i]

    # Append an element to the end of the list
    def append(self, e):
        if self.size < self.capacity:
            self.array[self.size] = e
        else:
            # Expand capacity if full
            self.expand_array_geom()
            self.array[self.size] = e
        self.size += 1

    # Remove element at index i
    def remove(self, i):
        return_value = self.get(i)  # Check for index validity
        # Shift elements left to fill the gap
        for j in range(i, self.size - 1):
            self.array[j] = self.array[j + 1]
        self.size -= 1

    # Replace element at index i with e
    def set(self, i, e):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        self.array[i] = e

    # Return number of elements in the list
    def get_size(self):
        return self.size

    # Return True if the list is empty
    def is_empty(self):
        return len(self.array) == 0
        # A more accurate implementation would be:
        # return self.size == 0

    # Expand array capacity arithmetically (+1000)
    def expand_array_arith(self):
        new_capacity = self.capacity + 1000
        new_array = np.empty(new_capacity, dtype=object)
        # Copy existing elements to new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # Expand array capacity geometrically (x2)
    def expand_array_geom(self):
        new_capacity = self.capacity * 2
        new_array = np.empty(new_capacity, dtype=object)
        # Copy existing elements to new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # Print all elements in the array
    def display(self):
        for i in range(self.get_size()):
            print(self.get(i), end=' ')

# Custom iterator for ArrayList
class ArrayListIterator:
    def __init__(self, array, size):
        self.cur_index = 0
        self.array = array
        self.size = size

    def __next__(self):
        # Check if end of list is reached
        if self.cur_index < self.size:
            return_value = self.array[self.cur_index]
            self.cur_index += 1
        else:
            raise StopIteration
        return return_value

# -----------------------------------------------
# Example usage
# -----------------------------------------------

# Create an instance of ArrayList
arr_list = ArrayList()

# Append elements 1 to 100
for i in range(1, 101):
    arr_list.append(i)

# Iterate and sum elements using custom iterator
total = 0
for item in arr_list:
    print(item)
    total += item

# Print total sum
print(total)
