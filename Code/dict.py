from node import Node

class CustomDictionary():

    def __init__(self, size):

        self.myBoard = {}
        self.boardSize = size

        for j in range(size):
            for i in range(size):
                self.myBoard[(i,j)] = Node((i,j))
        self.setNodeRelation()


    def getValFromDict(self, key):
        return self.myBoard[key]
    

    def setNodeRelation(self):
        for i in self.myBoard:
            
            up = (i[0] + 0, i[1] + -1)
            if self.coordInBoard(up):
                self.myBoard[i].setUp(self.myBoard[up])

            topRight = (i[0] + 1, i[1] + -1)
            if self.coordInBoard(topRight):
                self.myBoard[i].setTopRight(self.myBoard[topRight])

            right = (i[0] + 1, i[1] + 0)
            if self.coordInBoard(right):
                self.myBoard[i].setRight(self.myBoard[right])

            bottomRight = (i[0] + 1, i[1] + 1)
            if self.coordInBoard(bottomRight):
                self.myBoard[i].setBottomRight(self.myBoard[bottomRight])

            down = (i[0] + 0, i[1] + 1)
            if self.coordInBoard(down):
                self.myBoard[i].setDown(self.myBoard[down])   

            bottomLeft = (i[0] + -1, i[1] + 1)
            if self.coordInBoard(bottomLeft):
                self.myBoard[i].setBottomLeft(self.myBoard[bottomLeft])

            left = (i[0] + -1, i[1] + 0)
            if self.coordInBoard(left):
                self.myBoard[i].setLeft(self.myBoard[left])

            topLeft = (i[0] + -1, i[1] + -1)
            if self.coordInBoard(topLeft):
                self.myBoard[i].setTopLeft(self.myBoard[topLeft])


    def coordInBoard(self, A):
        if A[0] >= 0 and A[0] <= self.boardSize - 1 and A[1] >= 0 and A[1] <= self.boardSize - 1:
            return True
        return False
    