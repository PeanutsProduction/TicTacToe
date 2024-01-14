class Board:

    def __init__(self,givenSize):
        if givenSize <= 0:
            print("ERROR! Board size must be 3 or bigger \nSetting board size to 3 ... \n")
            givenSize = 3
        self.size = givenSize
        self.board = ['E' for i in range(self.size**2)]
        # dictonary coordinates test
        self.altBoard = {}
        for i in range(self.size):
            for j in range(self.size):
                self.altBoard[(i,j)] = "#"

    
    def __str__(self): # [1,2,3,1,2,3,1,2,3]
        line = ""
        counter = 1
        for i in self.altBoard:
            if counter == self.size:
                line += self.altBoard[i] + "\n"
                counter = 0
            else:
                line += self.altBoard[i] + "|"
            counter += 1
        print(line)
        return ""


            
    