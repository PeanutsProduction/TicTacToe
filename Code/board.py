class Board:

    def __init__(self,givenSize):
        if givenSize <= 0:
            print("ERROR! Board size must be 3 or bigger \nSetting board size to 3 ... \n")
            givenSize = 3
        self.size = givenSize

        # dictonary coordinates
        self.altBoard = {}
        for j in range(self.size):
            for i in range(self.size):
                self.altBoard[(i,j)] = None


        self.turnsDone = 0 # how many turns have happened

        # transformations in terms of compass
        self.N = (0,-1)
        self.S = (0,1)
        self.E = (1,0)
        self.W = (-1,0)
        self.NE = (1,-1)
        self.SE = (1,1)
        self.NW = (-1,-1)
        self.SW = (-1,1)


    def __str__(self): # [1,2,3,1,2,3,1,2,3]
        line = ""
        counter = 1
        for j in range(self.size):
            for i in range(self.size):
                x = "#"
                if self.altBoard[(i,j)] != None:
                    x = self.altBoard[(i,j)]

                if i == self.size - 1:
                    line += x + "\n"
                else:
                    line += x + "|"
        
        print(line)
        return ""


    def getSize(self):
        return self.size
    

    def setVal(self, coord, valToSet): # e.g setVal((0,1), "O")
        if type(coord) is not tuple:
            print("ERROR! Please pass a tuple")

        if self.altBoard[coord] == None:
            self.altBoard[coord] = valToSet
            #print("placed")
            return True
        else:
            #print("something there")
            return False
        

    def tupleAdder(self, A, B):
        return (A[0] + B[0], A[1] + B[1])
        
    
    def checkWin(self, coord, playerSide): # playerSide is "O" or "X"
        if self.verticalWin(coord, playerSide) or self.horizontalWin(coord, playerSide) or self.diagonalWin(coord, playerSide):
            return True
        return False


    def verticalWin(self, coord, playerSide):
        start = checker = coord
        while checker[1] != 0:
            checker = self.tupleAdder(checker, self.N)
            if self.altBoard[checker] != playerSide:
                return False
        checker = start

        while checker[1] != self.size - 1:
            checker = self.tupleAdder(checker, self.S)
            if self.altBoard[checker] != playerSide:
                return False
            
        return True
    
    
    def horizontalWin(self, coord, playerSide):
        start = checker = coord
        while checker[0] != 0:
            checker = self.tupleAdder(checker, self.W)
            if self.altBoard[checker] != playerSide:
                return False
        checker = start

        while checker[0] != self.size - 1:
            checker = self.tupleAdder(checker, self.E)
            if self.altBoard[checker] != playerSide:
                return False
            
        return True
    

    def diagonalWin(self, coord, playerSide):
        start = checker = coord
        
        diagonal1 = True # diagonal from top left to bottom right
        diagonal2 = True # diagonal from top right to bottom left

        while checker != (0,0):
            checker = self.tupleAdder(checker, self.NW)
            if self.altBoard[checker] != playerSide:
                diagonal1 = False
                break
        checker = start

        while checker != (self.size - 1, self.size - 1):
            checker = self.tupleAdder(checker, self.SE)
            if self.altBoard[checker] != playerSide:
                diagonal1 = False
                break

        if diagonal1 == True:
            return True


        while checker != (self.size - 1,0):
            checker = self.tupleAdder(checker, self.NE)
            if self.altBoard[checker] != playerSide:
                diagonal2 = False
                break
        checker = start

        while checker != (0, self.size - 1):
            checker = self.tupleAdder(checker, self.SW)
            if self.altBoard[checker] != playerSide:
                diagonal2 = False
                break
        
        if diagonal2 == True:
            return True
        
        elif diagonal1 == diagonal2 == False:
            return False
        