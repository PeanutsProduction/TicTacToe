from board import Board
import tkinter as tk
from tk import *

test = Board(3)
print(test)

# Create window named ui and setting somestuff
ui = tk.Tk()
ui.title("TicTacToe")
ui.iconbitmap(".\Resources\logo.ico")

# Parameters for setting window size and position
ui_width = 500 # min/default is 500
ui_height = 500 # min/default is 500

# Screen size of user
screen_width = ui.winfo_screenwidth()
screen_height = ui.winfo_screenheight()

# position for window on screen which is converted to int so we dont get error for decimals from ui.geometry
x = int(screen_width/2 - ui_width/2)
y = int(screen_height/2 - ui_height/2)

# Set window size
ui.geometry("{}x{}+{}+{}".format(ui_width, ui_height, x, y))

# Runs window
ui.mainloop()