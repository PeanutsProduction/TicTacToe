class Board:

    def __init__(self,x):
         self.size = x
         self.board = ['E' for i in range(self.size**2)]

    
    def __str__(self): # [1,2,3,1,2,3,1,2,3]
        line = ""
        counter = 1
        for i in self.board:
            if counter == self.size:
                line += i + "\n"
                counter = 0
            else:
                line += i + "|"
            counter += 1
        print(line)
        return "BOARD LOADED"

            
    