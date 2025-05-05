class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.header = Node(None)
        self.trailer = Node(None, self.header)
        self.header.next = self.trailer
        self.size = 0

    def add_first(self, value):
        new_node = Node(value, self.header, self.header.next)
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value, self.trailer.prev, self.trailer)
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        self.size += 1

    def last(self):
        if self.size == 0:
            raise IndexError("List is empty")
        return self.trailer.prev

    def first(self):
        if self.size == 0:
            raise IndexError("List is empty")
        return self.header.next

    def get_size(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return '[]'
        return_val = '['
        cur = self.header.next
        while cur is not self.trailer:
            return_val += str(cur.value) + ' '
            cur = cur.next
        return_val = return_val[:-1]
        return_val += ']'
        return return_val

    def remove_between(self, node1, node2):
        if node1 == None or node2 == None:
            raise ValueError("Node cannot be None")
        value = node1.next.value
        node1.next = node2
        node2.prev = node1
        return value

    def remove_first(self):
        value = self.remove_between(self.header, self.header.next.next)
        self.size-=1
        return value

    def remove_last(self):
        value = self.remove_between(self.trailer.prev.prev, self.trailer)
        self.size-=1
        return value

    def is_empty(self):
        return self.size == 0

    def search(self, value):
        curr = self.header.next
        index = 0
        while curr != self.trailer:
            if curr.value == value:
                return index
            curr = curr.next
            index += 1
        return -1

def dll_tester():
    test_list = DoublyLinkedList()
    assert test_list.get_size() == 0, 'list should be empty to start!'
    test_list.add_first(1)
    assert test_list.first().value == 1, 'add_first needs adjustment!'
    assert test_list.last().value == 1, 'add_first needs adjustment!'
    assert test_list.get_size() == 1, 'add_first needs adjustment!'
    test_list.add_first(2)
    assert test_list.first().value == 2, 'add_first needs adjustment!'
    assert test_list.last().value == 1, 'add_first needs adjustment!'
    assert test_list.get_size() == 2, 'add_first needs adjustment!'
    test_list.add_last(3)
    assert test_list.first().value == 2, 'add_last needs adjustment!'
    assert test_list.last().value == 3, 'add_last needs adjustment!'
    assert test_list.get_size() == 3, 'add_last needs adjustment!'
    assert test_list.remove_first() == 2, 'remove_first1 needs adjustment!'
    assert test_list.first().value == 1, 'remove_first2 needs adjustment!'
    assert test_list.last().value == 3, 'remove_first3 needs adjustment!'
    assert test_list.get_size() == 2, 'remove_first4 needs adjustment!'
    assert test_list.remove_last() == 3, 'remove_last needs adjustment!'
    assert test_list.first().value == 1, 'remove_last needs adjustment!'
    assert test_list.last().value == 1, 'remove_last needs adjustment!'
    assert test_list.get_size() == 1, 'remove_last needs adjustment!'
    while not test_list.is_empty():
        test_list.remove_first()
    assert test_list.get_size() == 0, 'list should be empty after removing all values'    
    for i in range(10):
        test_list.add_last(i+1)
    assert test_list.search(5) == 4, 'search(5) should return the index 4'
    assert test_list.search(20) == -1, 'search(20) should return -1 since 20 is not in the list'
    print('All tests passed!')

dll_tester()
