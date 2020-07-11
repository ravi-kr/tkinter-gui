from tkinter import *
root = Tk()
root.title("GUI Course")
root.geometry("800x500+200+80")
#root.config(bg = "#262626")
root.resizable(False, False)

def get_data():
    print(check_var.get())

check_var = StringVar()
check_ = Checkbutton(root, text = "ACCEPT?NOT", font = ("times new roman", 25, "bold"), onvalue = "On", offvalue = "Off", variable = check_var).place(x = 260, y = 150)
check_var.set("Off")
btn = Button(root, text = "SHOW", font = ("times new roman", 25, "bold"), bg = "lightgray", command = get_data).place(x = 260, y = 200, width = 150, height = 50)






root.mainloop()