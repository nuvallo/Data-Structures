"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.tail is None:
            return None  # if list is empty return none
        elif self.tail == self.head:  # only one node in list
            # could get either self.head or tail value since only one
            value = self.tail.get_value()
            self.head = None  # set both equal to none as to empty the list
            self.tail = None
            self.length -= 1  # subtract one from our length
            return value  # return value of removed node
        else:
            value = self.tail.get_value()
            # we know we have to iterate through a linked list, one way starting at head
            currentValue = self.head

            while currentValue.get_next() is not self.tail:  # while we are not on the tail node
                # value will be last node before tail, or while the currentValue is the same value or node as the tail
                currentValue = currentValue.get_next()

            self.tail = None  # set the tail to none to erase current tail
            self.tail = currentValue  # set the new tail to the node previously in front of the tail
            self.length -= 1
            return value  # return the value of the removed node

    def get_max(self):
        if not self.head and not self.tail:
            return None
        elif self.tail == self.head:
            # could also grab value of tail as only one node is both tail and head
            return self.head.get_value()
        else:
            currentMax = self.head.get_value()
            currentNode = self.head

            while currentNode.get_next() is not None:
                neighborNode = currentNode.get_next()
                if neighborNode.get_value() > currentMax:
                    currentMax = neighborNode.get_value()
                currentNode = currentNode.get_next()

            return currentMax

    def contains(self, value):
        if not self.head and not self.tail:
            return None
        elif self.tail == self.head:
            if self.head.get_value() == value:
                return True
            else:
                return False
        else:
            currentNode = self.head
            count = 0
            while count < self.length:
                #print(currentNode.get_value(), 'values')
                if currentNode.get_value() == value:
                    return True

                currentNode = currentNode.get_next()
                count += 1


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass
