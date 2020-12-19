class Node:
    # the basic structure of node
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    # this holds a reference to the very fist node in the list
    # self head is the last node in the list
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    # then we start to add elements in
    def append(self, data):
        # put the data in a node
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            # making sure current is the pointing at the last element
            while current.next:
                current = current.next
            # then we append
            current.next = node

    # this is faster because we not only store the reference to
    # not only the first node but also the last node in line
    def faster_append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    """
    def size(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count
    """

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail == current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
        prev = current
        current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None


class CircularLinkedList(object):
    def init(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = Node

        # this line makes it circular
        self.head.next = self.tail
        self.count += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail

        # when this is the first node or when we reach
        # the end of the list
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    # what makes circular linked list special
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                    self.count -= 1
        return
        prev = current
        current = current.next


"""
Run to test
"""
words = SinglyLinkedList()
words.append('foo')
words.append('bar')
words.append('bim')
words.append('baz')
words.append('quux')

print("access by index")
print("here is a node: {}".format(words[1]))

print("modify by index")
words[4] = "Quux"
print("Modified node by index: {}".format(words[4]))

print("This list has {} elements.".format(words.count))
for word in words.iter():
    print("Got this data: {}".format(word))

if words.search('foo'):
    print("Found foo in the list.")
if words.search('amiga'):
    print("Found amiga in the list.")

print("Now we try to delete an item")
words.delete('bim')
print("List now has {} elements".format(words.count))
for word in words.iter():
    print("data: {}".format(word))

print("delete the first item in the list")
words.delete('foo')
print("size: {}".format(words.count))
for word in words.iter():
    print("data: {}".format(word))

print("delete the last item in the list")
words.delete('quux')
print("size: {}".format(words.count))
for word in words.iter():
    print("data: {}".format(word))
