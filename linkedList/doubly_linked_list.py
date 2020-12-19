class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def init(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            #there are 2 pointers in 1 node
            #Therefore, we need to connect them twice
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

    def delete(self, data):
        """
        4 scenarios in delete operation:
            - search item not found 
            - search item located at the start of the list
            - search item located at the end of the list
            - search item located in the middle of the list
        """
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        while current:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                node_deleted = True
            current = current.next
        if node_deleted:
            self.count -= 1

    def iter(self):
        #self.tail points to the first varaible in the list
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False
