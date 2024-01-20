import math
import tkinter
from tkinter import *
from board import Board # import Board class from board file


class UIHandler:
    
    def __init__(self, whoStarts):

        self.board = None

        self.textColor = "white"
        self.font = "Arial"
        self.bgColor = "skyblue"

        self.mw = Tk()
        self.mw.resizable(False,False) # Make width and height non resizeable
        self.mw.title("TicTacToe")
        self.mw.iconbitmap(".\Resources\logo.ico") # logo
        self.mw.config(bg = self.bgColor)
        self.screenDimensions = self.getScreenSize()

        # Parameters for setting window size and position
        mainmenu_width = round(self.screenDimensions[0] * 0.25)
        mainmenu_height = round(self.screenDimensions[1] * 0.5)

        # position for window on screen which is converted to int so we dont get error for decimals from ui.geometry
        x = round(self.screenDimensions[0]/2 - mainmenu_width/2)
        y = round(self.screenDimensions[1]/2 - mainmenu_height/2)

        self.setWindowParameters(mainmenu_width, mainmenu_height, x, y)

        self.canvasGridIntervalsX = 0
        self.canvasGridIntervalsY = 0
        self.canvasGrid = None
        self.turn = StringVar()
        self.turn.set(whoStarts)
        
        self.mainmenu()
        self.mw.mainloop()


    def getScreenSize(self):
        temp = Tk()
        sizes = [temp.winfo_screenwidth(),temp.winfo_screenheight()]
        temp.destroy()
        return sizes
    
    
    def setWindowParameters(self, sizeX, sizeY, PosX, PosY):
        self.mw.geometry("{}x{}+{}+{}".format(round(sizeX), round(sizeY), PosX, PosY))


    def mainmenu(self):
        
        framePercentage = 0.9
        mm_Frame = Frame(
            self.mw, 
            width = round(self.mw.winfo_width() * framePercentage), 
            height = round(self.mw.winfo_height() * framePercentage), 
            bg = self.bgColor
        )
        mm_Frame.place(in_=self.mw, anchor="center", relx = 0.5, rely = 0.5)
        
        # Text
        gameNameText = Label(
            mm_Frame, 
            text = "TIC-TAC-TOE", 
            bg = self.bgColor,
            fg = self.textColor,
            anchor = "n",
            bd = 0,
            underline = len("TIC-TAC-TOE"),
            font=(self.font, 25)
        )
        gameNameText.grid(row = 0, column = 0, padx = 15, pady = 20) # grid

        # Buttons
        startGameButton = Button(mm_Frame, command = lambda: self.chooseSizeMenu(mm_Frame), text="Start Game", bg = self.bgColor, fg = self.textColor, relief = "flat", font=(self.font, 15), activebackground = self.bgColor, activeforeground = self.textColor)
        exitButton = Button(mm_Frame, command = self.mw.quit, text = "Exit", bg = self.bgColor, fg = self.textColor, relief = "flat", font=(self.font, 15), activebackground = self.bgColor, activeforeground = self.textColor)

        startGameButton.grid(row = 1, column = 0, padx = 15, pady = 20) # grid
        exitButton.grid(row = 2, column = 0, padx = 15, pady = 20) # grid


    def chooseSizeMenu(self, oldFrame):
        oldFrame.destroy()
        
        newSizeX = (self.screenDimensions[0] * 0.25)
        newSizeY = (self.screenDimensions[1] * 0.2)
        xPos = self.mw.winfo_x() + round(((self.screenDimensions[0] * 0.25) - (newSizeX))/2)
        yPos = self.mw.winfo_y() + round(((self.screenDimensions[1] * 0.5) - (newSizeY))/2)
        self.mw.geometry("{}x{}+{}+{}".format(round(newSizeX), round(newSizeY), xPos, yPos))

        newFrame = Frame(self.mw, bg = self.bgColor)
        newFrame.place(in_=self.mw, anchor="center", relx = 0.5, rely = 0.5)
        
        # Text
        sliderText = Label(newFrame, text = "Select board size", font = (self.font, 20), fg = self.textColor, bg = self.bgColor)
        sliderText.grid(row = 0, column = 0, padx = newSizeX/4, pady = newSizeY/16)

        sliderLength = newSizeX * 0.8
        #Slider
        boardSizeSlider = Scale( # Min board size and max board size
            newFrame, 
            from_ = 3, 
            to = 10,
            relief = "flat",
            highlightthickness = 0,
            highlightcolor = self.bgColor,
            borderwidth = 1,
            font = (self.font, 10), 
            bg = self.bgColor,
            fg = self.textColor,
            orient = HORIZONTAL,
            length = round(sliderLength),
            troughcolor = self.bgColor,
            )
        boardSizeSlider.place(in_=newFrame, anchor="center", relx = 0.5, rely = 0.5)
        boardSizeSlider.grid(row = 1, column = 0, padx = (newSizeX - sliderLength)/2, pady = newSizeY/16)

        # Slider Button
        sliderButton = Button(
            newFrame, 
            command = lambda: [self.createBoard(boardSizeSlider.get()), self.Game(boardSizeSlider.get(),newFrame)], 
            text = "Confirm",
            bg = self.bgColor, 
            fg = self.textColor, 
            relief = "flat", 
            font = (self.font, 15), 
            activebackground = self.bgColor, 
            activeforeground = self.textColor
            )
        sliderButton.grid(row = 2, column = 0, padx = newSizeX/4, pady = newSizeY/16)
    

    def Game(self, sliderVal, oldFrame):
        oldFrame.destroy()

        newSizeX = newSizeY = (self.screenDimensions[0] * 0.35)
        xPos = self.mw.winfo_x() + round(((self.screenDimensions[0] * 0.25) - (newSizeX))/2)
        yPos = self.mw.winfo_y() + round(((self.screenDimensions[1] * 0.2) - (newSizeY))/2)
        self.mw.geometry("{}x{}+{}+{}".format(round(newSizeX), round(newSizeY), xPos, yPos))

        sizeMult = 0.8
        TurnLabelFrame = Frame(self.mw, bg = self.bgColor)
        TurnLabelText = Label(TurnLabelFrame, text = "Turn: ", font = (self.font, 20), bg = self.bgColor, fg = self.textColor)
        TurnLabelVar = Label(TurnLabelFrame, textvariable = self.turn, font = (self.font, 20), bg = self.bgColor, fg = self.textColor)
        TurnLabelFrame.place(in_=self.mw, anchor="center", relx = 0.5 , y = self.mw.winfo_y() * 0.075)
        TurnLabelText.grid(row = 0, column = 0)
        TurnLabelVar.grid(row = 0, column = 1)

        gameCanvas = Canvas(bg = self.bgColor, width = newSizeX * sizeMult, height = newSizeY * sizeMult, bd = 0)
        self.canvasGrid = gameCanvas
        gameCanvas.place(in_=self.mw, anchor="center", relx = 0.5, rely = 0.5)
        
        self.mw.update() # IMPORTANT update before using winfo width and height
        self.canvasGridIntervalsX = round(gameCanvas.winfo_width()/sliderVal)
        self.canvasGridIntervalsY = round(gameCanvas.winfo_height()/sliderVal)

        
        for i in range(1, sliderVal): #Rows
            yOffset = (self.canvasGridIntervalsY * i)
            gameCanvas.create_line(0 , yOffset, gameCanvas.winfo_width(), yOffset, fill = self.textColor, width = 2)
        for j in range(1, sliderVal): #Columns
            xOffset = (self.canvasGridIntervalsX * j)
            gameCanvas.create_line(xOffset , 0, xOffset, gameCanvas.winfo_height(), fill = self.textColor, width = 2)


        gameCanvas.bind("<Button-1>", self.callback)


    def callback(self, event):
        #print ("clicked at", event.x, event.y)
        print("thats square", math.floor(event.x/self.canvasGridIntervalsX), math.floor(event.y/self.canvasGridIntervalsY), "\n")
        self.playerDoTurn((math.floor(event.x/self.canvasGridIntervalsX), math.floor(event.y/self.canvasGridIntervalsY)))
        self.switchTurn()


    def switchTurn(self):
        if self.turn.get() == "O":
            self.turn.set("X")
        elif self.turn.get() == "X":
            self.turn.set("O")


    def createBoard(self, size):
        self.board = Board(size)

    
    def playerDoTurn(self, coord):
        if self.board.setVal(coord, self.turn.get()):
            self.placePlayerSideOnButton(coord)
            self.board.turnsDone += 1
            if self.board.turnsDone > ((self.board.size - 1) * 2):
                self.board.checkWin(coord, self.turn.get())
            self.switchTurn()


    def placePlayerSideOnButton(self, coord):
        x = (self.canvasGridIntervalsX/2) + (self.canvasGridIntervalsX * coord[0])
        y = (self.canvasGridIntervalsY/2) + (self.canvasGridIntervalsY * coord[1])

        if self.turn.get() == "O":
            self.create_circle(x, y, self.sizeOfIconsOnGrid())
        elif self.turn.get() == "X":
            self.create_cross(x, y, self.sizeOfIconsOnGrid())

        print(self.board)
        self.switchTurn()
        

    def sizeOfIconsOnGrid(self):
        x = self.canvasGridIntervalsX
        if self.canvasGridIntervalsX > self.canvasGridIntervalsY:
            x = self.canvasGridIntervalsY
        return x * 0.3


    def create_circle(self, x, y, r): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.canvasGrid.create_oval(x0, y0, x1, y1, outline = self.textColor, width = 2)

    
    def create_cross(self, x, y, r):
        self.canvasGrid.create_line(x - r, y + r, x + r, y - r, fill = self.textColor, width = 2)
        self.canvasGrid.create_line(x + r, y + r, x - r, y - r, fill = self.textColor, width = 2)