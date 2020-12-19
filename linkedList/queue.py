#List based
class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
    def enqueue(self, data):
        #this is in contrasted to append()
        #insert makes it FIFO
        self.items.insert(0, data) 
        self.size += 1
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

#Stack-based
class Queue:
    def __init__(self):
        #to store elements added to the queue
        self.inbound_stack = []
        self.outbound_stack = []
    def enqueue(self, data):
        self.inbound_stack.append(data)
    def dequeue(self):
        #if the outbound stack is empty
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()


#Node-based, double linked list
class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class QueueNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            current = current.next
            current.prev = None
            self.count -= 1
    
