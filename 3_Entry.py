from tkinter import *
root = Tk()
root.title("GUI Course")
root.geometry("800x500+200+80")
root.config(bg = "#262626")
root.resizable(False, False)

def get_name():
    #print(txt_Entry.get())
    lbl_result.config(text = str(var_txt.get()))



var_txt = StringVar()


lbl_title = Label(root, text = "TITLE", font = ("Times New Roman", 40, "bold"), bg = "white", fg = "red").place(x= 0, y = 0, relwidth = 1)
txt_Entry = Entry(root, font = ("Times New Roman", 15, "bold"), bg = "lightyellow", fg = "black", textvariable = var_txt).place(x = 0, y = 60, width = 200)


btn_get = Button(root, text = "SHOW", font = ("Times New Roman", 25, "bold"), bg = "gray", fg = "white", activebackground = "gray", cursor = "hand2", command = get_name, activeforeground = "white").place(x = 100, y = 100, width = 150, height = 70)


address = Text(root).place(x = 50, y = 200, width = 400, height = 500)

lbl_result = Label(root, font = ("Times New Roman", 20, "bold"), bg = "#262626", fg = "white")
#lbl_result.place(x= 0, y = 200, relwidth = 1)



root.mainloop()