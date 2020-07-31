from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("GUI Layout")
root.geometry("1100x600+150+20")
root.config(bg = "#262626")

Window1 = Frame(root, bg = "lightgray", bd = 10, relief = GROOVE)
Window1.place(x = 0, y = 0, height = 340, width = 450)

show = Button(Window1,text = "Show").place(x = 50, y = 50)
show = Button(Window1, text = "Show").place(x = 250, y = 50)
show = Button(Window1, text = "Show").place(x = 50, y = 150)

Window2 = LabelFrame(root, text = "Student Details", font = ("times new roman", 20))
Window2.place(x = 550, y = 0, height = 340, width = 450)


root.mainloop()