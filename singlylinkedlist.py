import random

class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n
    def __repr__(self):
        return f"{self.value}"
    
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def is_empty(self)->bool:
        if self.head==None:
            return True
        else:
            return False
    
    def get_size(self)-> int:
        return self.size
        
        
    def add_first(self, v)->None:
        new_node=Node(v,self.head)
        self.head=new_node
        self.size+=1
        
    def __str__(self) -> str:
        if self.is_empty():
            return '[]'
        return_val = '['
        cur = self.head
        while cur is not None:
            return_val += str(cur.value) + ' '
            cur = cur.next
        return_val = return_val[:-1]
        return_val += ']'
        return return_val
    
    def add_last(self, t):
        if self.is_empty():
            self.add_first(t)
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        new_node = Node(t, None)
        curr.next = new_node
        self.size += 1  
        return new_node.value  
        
                
    def get(self,i:int)->object:
        if self.head is None:
            return ValueError
        if not isinstance(i,int) or i<0 or i>=self.size:
            raise IndexError
        # OTHER THAN THAT MAKE IT HAPPEN!!
        curr=self.head
        for _ in range(i):
            curr=curr.next
        return curr.value
    
    def rotate(self,n:int):
        pass
        
    def remove_at_index(self,i:int)->object:
        if self.head is None:
                raise ValueError("List is empty")
        if not isinstance(i, int) or i < 0 or i >= self.size:
            raise IndexError("Index out of range")
        if i == 0:
            removed_value = self.head.value
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(i - 1):
                curr = curr.next
            removed_value = curr.next.value
            curr.next = curr.next.next
        self.size -= 1
        return removed_value


        #same as get but also removes index 
        
    
    def remove_first(self):
        removed=self.remove_at_index(0)
        return removed
        #use remove at index

    def remove_last(self):
        remove=self.remove_at_index(self.size-1)
        return remove
        #use remove at index
        
    
# def homework_driver():
#     random.seed(0)
#     testing_list= SinglyLinkedList()
#     for i in range(1,4):
#         testing_list.add_first(i * random.randint(0,10))
#         testing_list.add_last(i * random.randint(0,10))
#         testing_list.add_first(i * random.randint(0,10))
#         testing_list.add_last(i * random.randint(0,10))
#     # print(TestingList)
#     for _ in range(5):
#         rand_index=random.randint(0,20)
#         # print(f'rand_index is {rand_index}')
#         try: testing_list.remove_at_index(rand_index)
#         except IndexError as e:
#             pass
#             # print(e)
#     print(testing_list)

# #The following is the main code block:
# homework_driver()
