from tkinter import *
root = Tk()
root.title("GUI LAYOUT")
root.geometry("800x500+250+50")

Frame1 = Frame(root, bd = 2, relief = RIDGE)
Frame1.place(x = 250, y = 50, height = 300, width = 200)

scrolly = Scrollbar(Frame1, orient = VERTICAL)
scrolly.pack(side = RIGHT, fill = Y)

data = Listbox(Frame1, font = ("times new roman", 20), justify = CENTER, yscrollcommand = scrolly.set)
data.pack()
scrolly.config(command = data.yview)

for i in range(0,101):
    data.insert(i, "Data: "+str(i))

root.mainloop()