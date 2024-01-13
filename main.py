class Board:

    def __init__(self,x,y):
         self.sizeX = x
         self.sizeY = y
         self.board = [["1" for i in range(self.sizeX)] for i in range(self.sizeY)]

    
    def __str__(self):
        for i in range(self.sizeY):
            line = ""
            for j in range(self.sizeX):
                line += self.board[i][j] + " "
            print(line)


test = Board(3,3)
print(test)
#comment test

            
    