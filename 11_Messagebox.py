from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI Layout")
root.geometry("800x500+250+50")
root.config(bg = "#262626")

def message():
    messagebox.showerror("Show error message", "This is show error message box")

def message2():
    messagebox.showinfo("Show info message", "This is show info message box")

def message3():
    messagebox.showwarning("Show warning message", "This is show warning message box")


btn_1 = Button(root, text = "Message 1", command = message).place(x = 50, y = 50, height = 40, width = 200)
btn_2 = Button(root, text = "Message 2", command = message2).place(x = 260, y = 50, height = 40, width = 200)
btn_3 = Button(root, text = "Message 3", command = message3).place(x = 510, y = 50, height = 40, width = 200)





root.mainloop()