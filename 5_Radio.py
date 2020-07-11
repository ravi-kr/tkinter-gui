from tkinter import *
root = Tk()
root.title("GUI Course")
root.geometry("800x500+200+80")
#root.config(bg = "#262626")
root.resizable(False, False)


gender = Label(root, text = "Select Gender", font = ("times new roman", 20, "bold")).place(x =100, y = 50)

def gender_funct():
    print(gender.get())



gender = StringVar()
male = Radiobutton(root, text = "Male", value = "male", variable = gender, font = ("times new roman", 18, "bold")).place(x = 100, y = 150)
female = Radiobutton(root, text = "Female", value = "female", variable = gender, font = ("times new roman", 18, "bold")).place(x = 250, y = 150)
gender.set("male")


btn = Button(root, text = "SHOW", font = ("times new roman", 25, "bold"), command = gender_funct, bg = "lightgray").place(x = 260, y = 200, width = 150, height = 50)




root.mainloop()