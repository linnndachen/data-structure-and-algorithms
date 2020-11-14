from array2D import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self.grid = Array2D(numRows, numCols)
        self.grid.clear(0)

    def numRows(self):
        return self.grid.numRows()
    
    def numCols(self):
        return self.grid.numCols()
    
    def __getitem__(self, ndxTuple):
        return self.grid[ndxTuple[0], ndxTuple[1]]
    
    def __setitem__(self, ndxTuple, scalar):
        self.grid[ndxTuple[0], ndxTuple[1]]=scalar
    
    def scaleby(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    def transpose(self):
        pass

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(),\
                'incorrect size'
        
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r,c] + rhsMatrix[r,c]
        return newMatrix
    
    def __sub__(self, rhsMatrix):
        pass

    def __mul__(self, rhsMatrix):
        pass