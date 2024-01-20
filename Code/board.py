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
        self.N = (0, -1)
        self.S = (0, 1)
        self.E = (1, 0)
        self.W = (-1, 0)
        self.NE = (1, -1)
        self.SE = (1, 1)
        self.NW = (-1, -1)
        self.SW = (-1, 1)


    
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
        

    def tupleCalc(self, A, B):
        return (A[0] + B[0], A[1] + B[1])
        
    
    def checkWin(self, coord, playerSide): # playerSide is "O" or "X"
        return self.VerticalWin(coord, playerSide)


    def VerticalWin(self, coord, playerSide):
        start = checker = coord
        while checker[1] != 0:
            checker = self.tupleCalc(checker, self.N)
            if self.altBoard[checker] != playerSide:
                return False
        checker = start

        while checker[0] != self.size - 1:
            checker = self.tupleCalc(checker, self.S)
            if self.altBoard[checker] != playerSide:
                return False
            
        return True