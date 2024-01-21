class Node:
    
    def __init__(self, coord):
        self.data = None
        self.posCoord = coord

        self.up = None
        self.topRight = None
        self.right = None
        self.bottomRight = None
        self.down = None
        self.bottomLeft = None
        self.left = None
        self.topLeft = None

        self.relationDict = {
            "up": self.getUp,
            "topRight": self.getTopRight,
            "right": self.getRight,
            "bottomRight": self.getBottomRight,
            "down": self.getDown,
            "bottomLeft": self.getBottomLeft,
            "Left": self.getLeft,
            "topLeft": self.getTopLeft,
            }
    

    def setData(self, val):
        self.data = val
    def getData(self):
        return self.data
    

    def getPosCord(self):
        return self.posCoord


    def checkNextSquareSafe(self, dir, playerSide):
        method = self.relationDict[dir]
        nextSquare = method()
        return nextSquare != None and nextSquare.getData() != None and nextSquare.getData() == playerSide


    # up
    def setUp(self, v):
        self.up = v
    def getUp(self):
        return self.up
    
    # topRight
    def setTopRight(self, v):
        self.topRight = v
    def getTopRight(self):
        return self.topRight
    
    # right
    def setRight(self, v):
        self.right = v
    def getRight(self):
        return self.right
    
    # bottomRight
    def setBottomRight(self, v):
        self.bottomRight = v
    def getBottomRight(self):
        return self.bottomRight
    
    # down
    def setDown(self, v):
        self.down = v
    def getDown(self):
        return self.down
    
    # bottomLeft
    def setBottomLeft(self, v):
        self.bottomLeft = v
    def getBottomLeft(self):
        return self.bottomLeft
    
    # left
    def setLeft(self, v):
        self.left = v
    def getLeft(self):
        return self.left
    
    # topLeft
    def setTopLeft(self, v):
        self.topLeft = v
    def getTopLeft(self):
        return self.topLeft
    
    
        