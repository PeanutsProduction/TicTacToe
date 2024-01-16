from tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Button(root, bg = "skyblue", bd = 1, width = 10)
        b.grid(row=i, column=j)

root.mainloop()