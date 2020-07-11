from tkinter import *
root = Tk()
root.title("GUI Course")
root.geometry("800x500+200+80")
root.config(bg = "#262626")
root.resizable(False, False)


def show_data():

    var_data.set(str(text_field.get('1.0',END)))
    print(var_data.get())


var_data = StringVar()

text_field= Text(root)
text_field.place(x = 50, y = 200, width = 400, height = 500)

btn_get = Button(root, text = "SHOW", font = ("Times New Roman", 25, "bold"), bg = "gray", fg = "white", activebackground = "gray", cursor = "hand2", command = show_data, activeforeground = "white").place(x = 100, y = 100, width = 150, height = 70)


root.mainloop()