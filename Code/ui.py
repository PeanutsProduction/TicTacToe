import tkinter as tk
from tkinter import *

# root = Tk()
# root.title("title")
# root.geometry("500x500")
# root.update_idletasks()  # updates the width of the window
# root.config(bg = "skyblue")

# print(root.winfo_width())
# framePercentage = 0.9
# left_frame = Frame(root, width=round(root.winfo_width() * framePercentage), height=round(root.winfo_height() * framePercentage))
# left_frame.grid(row=0, column=0, padx=10, pady=5)
# left_frame.place(in_=root, anchor="center", relx = 0.5, rely = 0.5)
# root.mainloop()

# root = Tk()
# root.title("title")
# root.geometry("800x500")
# root.resizable(False,False)

# def window2():
#     root.destroy()
#     window2_main = Tk()
#     Label(window2_main, text="Bye Bye").pack()
#     window2_main.mainloop()
# a = Button(text="Click This", command=window2)
# a.pack()
# root.mainloop()



# root=tk.Tk()
# f1 = tk.Frame(width=200, height=200, background="red")
# f2 = tk.Frame(width=100, height=100, background="blue")

# f1.pack(fill="both", expand=True, padx=20, pady=20)
# f2.place(in_=f1, anchor="c", relx=.5, rely=.5)

# root.mainloop()

class UIHandler:

    def __init__(self):
        self.font = "Arial"
        self.bgColor = "skyblue"
        temp = Tk()
        self.screen_width = temp.winfo_screenwidth()
        self.screen_height = temp.winfo_screenheight()
        temp.destroy()

    
    def mainmenu(self):

        mm_textColor = "white"

        # Create window named ui and setting somestuff
        mw = tk.Tk()
        mw.resizable(False,False) # Make width and height non resizeable
        mw.title("TicTacToe")
        mw.iconbitmap(".\Resources\logo.ico") # logo
        mw.config(bg = self.bgColor)

        # Parameters for setting window size and position
        mainmenu_width = round(self.screen_width * 0.25)
        mainmenu_height = round(self.screen_height * 0.5)

        # position for window on screen which is converted to int so we dont get error for decimals from ui.geometry
        x = round(self.screen_width/2 - mainmenu_width/2)
        y = round(self.screen_height/2 - mainmenu_height/2)

        # Set window size
        mw.geometry("{}x{}+{}+{}".format(mainmenu_width, mainmenu_height, x, y))
        mw.update_idletasks()  # Updates the dimensions of the window

        # Create a frame
        framePercentage = 0.9
        mm_Frame = Frame(
            mw, 
            width = round(mw.winfo_width() * framePercentage), 
            height = round(mw.winfo_height() * framePercentage), 
            bg = self.bgColor
        )
        mm_Frame.place(in_=mw, anchor="center", relx = 0.5, rely = 0.5)
        
        # Text
        gameNameText = Label(
            mm_Frame, 
            text = "TIC-TAC-TOE", 
            bg = self.bgColor,
            fg = mm_textColor,
            anchor = "n",
            bd = 0,
            underline = len("TIC-TAC-TOE"),
            font=(self.font, 25)
        )
        gameNameText.grid(row = 0, column = 0, padx = 15, pady = 20) # grid
        
        # Buttons
        startGameButton = Button(mm_Frame, command = lambda: self.chooseSizeMenu(mm_Frame, mw), text="Start Game", bg = self.bgColor, fg = mm_textColor, relief = "flat", font=(self.font, 15))
        exitButton = Button(mm_Frame, command = mw.quit, text = "Exit", bg = self.bgColor, fg = mm_textColor, relief = "flat", font=(self.font, 15))

        startGameButton.grid(row = 1, column = 0, padx = 15, pady = 20) # grid
        exitButton.grid(row = 2, column = 0, padx = 15, pady = 20) # grid

        # Runs window
        mw.mainloop()


    # 2nd MENU
    def chooseSizeMenu(self, oldFrame, mw):
        oldFrame.destroy()
        
        newSizeX = (self.screen_width * 0.25)
        newSizeY = (self.screen_height * 0.2)
        xPos = mw.winfo_x() + round(((self.screen_width * 0.25) - (newSizeX))/2)
        yPos = mw.winfo_y() + round(((self.screen_height * 0.5) - (newSizeY))/2)
        mw.geometry("{}x{}+{}+{}".format(round(newSizeX), round(newSizeY), xPos, yPos))

        newFrame = Frame(mw, bg = self.bgColor)
        newFrame.place(in_=mw, anchor="center", relx = 0.5, rely = 0.5)
        
        # Text
        sliderText = Label(newFrame, text = "Select board size", font = (self.font, 20), fg = "white", bg = self.bgColor)
        sliderText.grid(row = 0, column = 0, padx = newSizeX/4, pady = newSizeY/16)

        sliderLength = newSizeX * 0.8
        # Slider
        boardSizeSlider = Scale( # Min board size and max board size
            newFrame, 
            from_ = 3, 
            to = 10,
            relief = "flat",
            bd = 1,
            bg = self.bgColor,
            orient = HORIZONTAL,
            length = round(sliderLength),
            troughcolor = self.bgColor
            )
        boardSizeSlider.place(in_=newFrame, anchor="center", relx = 0.5, rely = 0.5)
        boardSizeSlider.grid(row = 1, column = 0, padx = (newSizeX - sliderLength)/2, pady = newSizeY/16)

        # Slider Button
        sliderButton = Button(newFrame, command = lambda: self.Game(boardSizeSlider.get(),newFrame,mw), text = "Confirm")
        sliderButton.grid(row = 2, column = 0, padx = newSizeX/4, pady = newSizeY/16)



    def Game(self, sliderVal, oldFrame, mw):
        oldFrame.destroy()

        newSizeX = newSizeY = (self.screen_width * 0.35)
        xPos = mw.winfo_x() + round(((self.screen_width * 0.25) - (newSizeX))/2)
        yPos = mw.winfo_y() + round(((self.screen_height * 0.2) - (newSizeY))/2)
        mw.geometry("{}x{}+{}+{}".format(round(newSizeX), round(newSizeY), xPos, yPos))

        sizeMult = 0.8
        gameFrame = Frame(bg = "red", width = newSizeX * sizeMult, height = newSizeY * sizeMult, bd = 0)
        gameFrame.place(in_=mw, anchor="center", relx = 0.5, rely = 0.5)

        
        gameCanvas = Canvas(bg = self.bgColor, width = newSizeX * sizeMult, height = newSizeY * sizeMult, bd = 0)
        gameCanvas.place(in_=gameFrame, anchor="center", relx = 0.5, rely = 0.5)
        
        xintervals = round((newSizeX * sizeMult) + 10)/sliderVal
        yintervals = round((newSizeY * sizeMult) + 10)/sliderVal
        for i in range(1, sliderVal): #Rows
            gameCanvas.create_line(gameCanvas.winfo_x(),gameCanvas.winfo_y() + (yintervals * i),gameCanvas.winfo_x() + round(newSizeX * sizeMult), gameCanvas.winfo_y() + (yintervals * i), fill="green", width=5)
        for j in range(1, sliderVal): #Columns
            gameCanvas.create_line(gameCanvas.winfo_x() + (xintervals * j),gameCanvas.winfo_y(), gameCanvas.winfo_x() + (xintervals * j), gameCanvas.winfo_y() + round(newSizeY * sizeMult), fill="green", width=5)
                




