from array import Array

class Array2D:
    def __init__(self, numRows, numCols):
        self.theRows = Array(numRows)
        for i in range(numCols):
            self.theRows[i] == Array(numCols)

    def numRows(self):
        return len(self.theRows)

    def numCols(self):
        return len(self.theRows[0])

    def clear(self, value):
        for row in range(self.numRows):
            row.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows()\
            and col >=0 and col < self.numCols(), "out of index"

        onedArray = self.theRows[row]
        return onedArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows()\
            and col >=0 and col < self.numCols(), "out of index"

        onedArray = self.theRows[row]
        onedArray[col] = value

