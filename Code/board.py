from node import Node
from dict import CustomDictionary

class Board:

    def __init__(self,givenSize):
        if givenSize <= 0:
            print("ERROR! Board size must be 3 or bigger \nSetting board size to 3 ... \n")
            givenSize = 3
        self.size = givenSize

        # dictonary coordinates
        self.myBoard = CustomDictionary(self.size)

        self.winCon = 4 # how many in a row to win (minimum 3)
        self.turnsDone = 0 # how many turns have happened

        # coordinates to draw line over winning squares
        self.winLineStart = None
        self.winLineEnd = None


    def __str__(self): # [1,2,3,1,2,3,1,2,3]
        line = ""
        counter = 1
        for j in range(self.size):
            for i in range(self.size):
                x = "#"
                if self.myBoard.getValFromDict((i,j)) != None:
                    x = self.myBoard.getValFromDict((i,j))

                if i == self.size - 1:
                    line += x + "\n"
                else:
                    line += x + "|"
        
        print(line)
        return line


    def getSize(self):
        return self.size


    def setNodeRelations(self, Node):
        n = Node

        temp = n

        # above


    def setVal(self, coord, valToSet): # e.g setVal((0,1), "O")
        if type(coord) is not tuple:
            print("ERROR! Please pass a tuple")

        if self.myBoard.getValFromDict(coord).getData() == None:
            self.myBoard.getValFromDict(coord).setData(valToSet) 
            #print("placed")
            return True
        else:
            #print("something there")
            return False
        return False
        

    def setWinCon(self, num):
        self.winCon = num
        return


    def getWinLineCoords(self):
        return (self.winLineStart,self.winLineEnd)


    def getNode(self, A): # return Node
        return self.myBoard.getValFromDict(A)
              
    
    def checkWin(self, coord, playerSide): # playerSide is "O" or "X"
        if self.verticalWin(coord):
            return True
        return False


    def verticalWin(self, coord):
        playerSide = self.getNode(coord).getData()
        pointer1 = pointer2 = self.getNode(coord)
        counter = 1
        while counter != self.winCon:
            upSafe = pointer1.checkNextSquareSafe("up", playerSide)
            downSafe = pointer2.checkNextSquareSafe("down", playerSide)
            if upSafe:
                pointer1 = pointer1.getUp()
                counter += 1
            if downSafe:
                pointer2 = pointer2.getDown()
                counter += 1
                continue
            
            if upSafe == False and downSafe == False and counter !=  self.winCon:
                return False
            
        self.winLineStart = pointer1.getPosCord()
        self.winLineEnd = pointer2.getPosCord()
        return True
    
    
    def horizontalWin(self, coord):
        playerSide = self.getNode(coord).getData()
        pointer1 = pointer2 = self.getNode(coord)
        counter = 1
        while counter != self.winCon:
            leftSafe = pointer1.checkNextSquareSafe("left", playerSide)
            rightSafe = pointer2.checkNextSquareSafe("right", playerSide)
            if leftSafe:
                pointer1 = pointer1.getLeft()
                counter += 1
            if rightSafe:
                pointer2 = pointer2.getRight()
                counter += 1
                continue
            
            if leftSafe == False and rightSafe == False and counter !=  self.winCon:
                return False
            
        self.winLineStart = pointer1.getPosCord()
        self.winLineEnd = pointer2.getPosCord()
        return True
    

    # def diagonalWin(self, coord, playerSide):
    #     start = checker = coord
        
    #     diagonal1 = True # diagonal from top left to bottom right
    #     diagonal2 = True # diagonal from top right to bottom left

    #     while checker != (0,0):
    #         checker = self.tupleAdder(checker, self.NW)
    #         try:
    #             if self.myBoard[checker] != playerSide:
    #                 diagonal1 = False
    #                 break
    #         except:
    #             diagonal1 = False
    #             break
    #     checker = start

    #     while checker != (self.size - 1, self.size - 1):
    #         checker = self.tupleAdder(checker, self.SE)
    #         try:
    #             if self.myBoard[checker] != playerSide:
    #                 diagonal1 = False
    #                 break
    #         except:
    #             diagonal1 = False
    #             break

    #     if diagonal1 == True:
    #         return True


    #     while checker != (self.size - 1,0):
    #         checker = self.tupleAdder(checker, self.NE)
    #         try:
    #             if self.myBoard[checker] != playerSide:
    #                 diagonal2 = False
    #                 break
    #         except:
    #             diagonal2 = False
    #             break
    #     checker = start

    #     while checker != (0, self.size - 1):
    #         checker = self.tupleAdder(checker, self.SW)
    #         try:
    #             if self.myBoard[checker] != playerSide:
    #                 diagonal2 = False
    #                 break
    #         except:
    #             diagonal2 = False
    #             break
        
    #     if diagonal2 == True:
    #         return True
        
    #     elif diagonal1 == diagonal2 == False:
    #         return False
        