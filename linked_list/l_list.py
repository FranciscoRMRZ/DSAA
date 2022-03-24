#! python3

class Node(object):
    '''Node class'''
    def __init__(self):
        self.index = 0
        self.next = None
        self.payload = None
        self.previous = None


class Linked_list():
    ''' Linked list class'''
    def __init__(self):
        self.item_count = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.item_count

    def add_node(self, payload):
        new_node = Node()
        new_node.payload = payload
        if self.head == None:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        self.item_count += 1

    def del_head(self):
        if self.item_count == 0:
            raise IndexError('delete head from an empty linked list')
        self.head = self.head.next
        self.item_count -= 1
        
    def traverse(self):
        node = self.head
        while node:
            print(node.payload)
            node = node.next


class D_linked_list():
    '''Doubly linked list'''
    def __init__(self):
        self.item_count = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.item_count
    
    def __getitem__(self, arg):
        # TODO: 
        # implement a get item method to use square brackets for slicing 
        # and element selection.
        raise NotImplementedError('function not implemented')

    def fix_index(self):
        self.head.index = 0
        node = self.head
        while node:
            if node.previous:
                node.index = node.previous.index + 1
            node = node.next

    def insert(self, payload):
        '''Insert a new element into the list'''
        new_node = Node()
        new_node.payload = payload
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        new_node.previous = None
        self.head.index = self.item_count
        self.item_count += 1

    def search_index(self, search_index=0):
        '''Search for a specific node by index'''
        node = self.head
        while node and node.index != search_index:
            node = node.next
        return node #.payload if node else None
    
    def delete(self, del_index=0):
        # raise NotImplementedError()
        del_node = self.search_index(del_index)
        if del_node.previous:
            del_node.previous.next = del_node.next
        else:
            self.head = del_node.next
        if del_node.next:
            del_node.next.previous = del_node.previous
        self.fix_index()
        self.item_count -= 1

    def traverse(self):
        node = self.head
        if node:
            yield node
            node = node.next

