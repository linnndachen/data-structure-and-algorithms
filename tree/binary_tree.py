"""
A regular binary tree satifies:
each node should have a maximum of 2 children

A Binary Search Tree Satisfies:
All nodes in the left sub-tree are <= the value of that node
All nodes in the right sub-tree are >= the value of that node
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

#binary search tree
class Tree:
    def __init__(self):
        self.root_node = None
    
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        #need to keep track of the current node that
        #we are comparing and its parent node
        else:
            current = self.root_node
            parent = None
        #while we still have nodes that we have not
        #compared with, we keep going
        while True:
            parent = current
            if node.data < parent.data:
                current = current.left_child
                if current is None:
                    parent.left_child = node
                    return 
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    """
    when we are considering removing a node, one important thing is to find the next biggest descendant of that deleted node. Therefore, let's go over search function first.
    """
    #almost equal to binary search
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    #this is the helper function for removal and
    #it returns with the parent node
    def get_node_with_parent(self, data):
        """
        If tree is empty, return (none, none)
        If the root node is bigger than the data:
            parent is the current node
            current is the left child
        if the root node is smaller than the data:
            parent is the current node
            current is the right child
        """
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        #to know how many children the node that we want to delete has
        child_count = 0
        if node.left_child and node.right_child:
            child_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            child_count = 0
        else:
            child_count = 1

        if child_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None

        elif child_count == 1:
            #next_node is the node that needs to be deleted
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            #reset all the nodes
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        #when have 2 children
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            #the node that we want to remove
            node.data = leftmost_node.data

            #update the nodes after we found that node that we want
            #to remove
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current