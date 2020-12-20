class MinHeap:
    """
    parent node must be smaller or equal to its children
    """
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    #helper methods
    def parent_index(self, idx):
        return idx // 2
    def left_child_index(self, idx):
        return idx * 2
    def right_child_index(self, idx):
        return idx * 2 + 1
    def child_present(self, idx):
        return self.left_child_index(idx) <= self.count

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        swap_count = 0
        while self.parent_index(idx) > 0:
            if self.heap_list[self.parent_index(idx)] > self.heap_list[idx]:
                swap_count += 1
                tmp = self.heap_list[self.parent_index(idx)]
                self.heap_list[self.parent_index(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_index(idx)



    def get_smaller_child_idx(self, idx):
        if self.right_child_index(idx) > self.count:
            return self.left_child_index(idx)
        else:
            left_child = self.heap_list[self.left_child_index(idx)]
            right_child = self.heap_list[self.right_child_index(idx)]
            if left_child < right_child:
                return self.left_child_index
            else:
                return self.right_child_index

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
                idx = smaller_child_idx

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        #remove min from the list
        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        #last element moved to the first
        self.heap_list.pop()
        self.heapify_down()
        return min
