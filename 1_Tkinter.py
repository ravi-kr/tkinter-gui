#import tkinter as tk

#root = tk.Tk()
#root.mainloop()

from tkinter import *

root = Tk()
root.title("GUI Course")
root.geometry("800x400+200+50")
root.resizable(False, False)
root.config(bg = "#262626")
# GRID SYSTEM
#lbl = Label(root, text = 'GRID SYSTEM').grid(row = 0, column = 0)
#lbl = Label(root, text = 'GRID SYSTEM').grid(row = 0, column = 1)
#lbl = Label(root, text = 'GRID SYSTEM').grid(row = 2, column = 0)

# Pack SYSTEM
#lbl = Label(root, text = 'Pack1 SYSTEM').pack(side = LEFT)
#lbl = Label(root, text = 'Pack2 SYSTEM WITH FILL').pack(expand = 1, fill = BOTH)
#lbl = Label(root, text = 'Pack normal SYSTEM').pack()

# Place SYSTEM
lbl = Label(root, text = 'Place SYSTEM').place(x = 0, y = 0)
lbl = Label(root, text = 'Place SYSTEM').place(x = 400, y = 300)
lbl = Label(root, text = 'Place SYSTEM').place(x = 200, y = 200)

root.mainloop()