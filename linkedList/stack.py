class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#node based - singly linked list
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1


    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

#dynamic array
class Stack_list:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()


"""
Stack question
"""
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

def calc(node):
    if node.data is "+":
        return calc(node.left) + calc(node.right)
    elif node.data is "-":
        return calc(node.left) - calc(node.right)
    elif node.data is "*":
        return calc(node.left) * calc(node.right)
    elif node.data is "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    stack.push(node)

root = stack.pop()
result = calc(root)
print(result)