from tkinter import *
from tkinter import ttk


root = Tk()
root.title("GUI Layout")
root.geometry("800x500+250+50")

def get_data():
    print(language.get())

language = ttk.Combobox(root, values = ("PHP", "Python", "C++", "Java", "HTML"), font = ("times new roman", 20, "bold"), justify = CENTER, state = "readonly")
language.place(x  = 100, y = 50, width = 200, height = 40)
language.set("Select language")

btn = Button(root, text = "SHOW", command = get_data).place(x = 50, y = 200)

root.mainloop()
