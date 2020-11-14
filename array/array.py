#id array
class Array:
    def __init__(self, size, arrayType = int):
        assert size >0, 'Array size must be > 0'
        self.size = size
        self.items = [arrayType(0)] * size
        self.arrayType = arrayType

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), IndexError
        return self.items[ index ]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), IndexError
        self.items[ index ] = value

    def clear(self, value):
        for i in range(len(self)):
            self.items[i]=value

    def search(self, key, position):
        assert position < self.size, "out of range index"
        for i in range(self.size):
            if self.items[i] == key:
                return i
        return -1

    def insert(self, key, position):
        assert position < self.size, "out of range index"
        for i in range(self.size-2, position-1, -1):
            self.items[i+1] = self.items[i]
        self.items[position] = key

    def delete(self, key, position):
        assert position < self.size, "out of range index"
        for i in range(position, self.size-1):
            self.items[i] = self.items[i+1]
        self.items[i+1] = self.arrayType(0)

    def __iter__(self):
        return ArrayIterator(self.items)


class ArrayIterator:
    def __init__(self, theArray):
        self.arrayRef = theArray
        self.curdNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curdNdx < len(self.arrayRef):
            entry = self.arrayRef[self.curdNdx]
            self.curdNdx += 1
            return entry
        else:
            raise StopIteration
