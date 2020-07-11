from tkinter import *
root = Tk()
root.title("GUI Course")
root.geometry("400x500+700+80")
root.config(bg = "#262626")
root.resizable(False, False)

lbl_title = Label(root, text = "TITLE", font = ("Times New Roman", 40, "bold"), bg = "white", fg = "red").pack(fill = X)
lbl_title = Label(root, text = "TITLE2", font = ("Times New Roman", 40, "bold"), bg = "YELLOW", fg = "red", pady = 50, bd = 10, relief = GROOVE).pack(fill = X, pady = 20, padx = 20)
lbl_title = Label(root, text = "TITLE", font = ("Times New Roman", 40, "bold"), bg = "YELLOW", fg = "red").place(x = 150, y = 300, height = 200, width = 250)

root.mainloop()