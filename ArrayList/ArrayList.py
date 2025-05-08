import numpy as np
from time import time
class ArrayList:
    def __init__(self):
        self.capacity = 10  # initial capacity
        self.size = 0
        self.array = np.empty(self.capacity, dtype=object)
    def __iter__(self):
        return ArrayListIterator(self.array,self.size)
        


    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        return self.array[i]

    def append(self, e):
        if self.size<self.capacity:
            self.array[self.size]=e
        else:
            self.expand_array_geom()
            self.array[self.size]=e
        self.size += 1
    def remove(self, i):
        return_value=self.get(i)
        for j in range(i,self.size-1):
            self.array[j]=self.array[j+1]
            
        self.size-=1
        
    def set(self, i, e):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        self.array[i]=e

    def get_size(self):
        return self.size

    def is_empty(self):
        return len(self.array) == 0
        # if self.size==0:
        #     return True
        # return False
    
    def expand_array_arith(self):
        new_capacity=self.capacity+1000
        new_array=np.empty(new_capacity, dtype=object)
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array
        self.capacity=new_capacity
    def expand_array_geom(self):
        new_capacity=self.capacity*2
        new_array=np.empty(new_capacity, dtype=object)
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array
        self.capacity=new_capacity
    
    def display(self):
        for i in range(self.get_size()):
            print(self.get(i),end=' ')
class ArrayListIterator:
    def __init__(self,array,size):
        self.cur_index=0
        self.array=array
        self.size=size
    def __next__(self):
        if self.cur_index < self.size:
            return_value=self.array[self.cur_index]
            self.cur_index+=1
        else:
            raise StopIteration
        return return_value
    



# Create an instance of ArrayList
arr_list = ArrayList()

# Append some elements to the ArrayList
for i in range(1, 101):
    arr_list.append(i)


# Iterate through the ArrayList using the iterator
total=0
for item in arr_list:
    print(item)
    total+=item
print(total)