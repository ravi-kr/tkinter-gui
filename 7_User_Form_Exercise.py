from tkinter import *
root = Tk()
root.title("GUI Layout")
root.geometry("800x500+250+50")


var_username = StringVar()
var_email = StringVar()
var_gender = StringVar()
var_check = IntVar()


title = Label(root, text = "User Entry Form", font = ("Impact", 30), bg = "#262626", fg = "white").place(x = 0, y = 0, relwidth = 1)

def get_data():
    if var_check.get() == 1:
        result = "Username: " + var_username.get() + ", " + "\tEmail: " + var_email.get() + ", " +"\tGender: "+ var_gender.get()
        lbl_result.config(text = str(result))
    else:
        lbl_result.config(text="Please accept Terms and Conditions")

lbl_username = Label(root, text = "Username", font = ("times new roman", 30)).place(x = 50, y = 100)
lbl_email = Label(root, text = "E-mail", font = ("times new roman", 30)).place(x = 50, y = 150)
lbl_gender = Label(root, text = "Gender", font = ("times new roman", 30)).place(x = 50, y = 200)

txt_username = Entry(root, textvariable = var_username, font = ("times new roman", 15)).place(x = 250, y = 100, width = 400, height = 35)
txt_email = Entry(root, textvariable = var_email,font = ("times new roman", 15)).place(x = 250, y = 150, width = 400, height = 35)

male = Radiobutton(root, variable = var_gender,text = "Male", value = "male", font = ("times new roman", 20)).place(x = 250, y = 200)
female = Radiobutton(root, variable = var_gender,text = "Female", value = "female", font = ("times new roman", 20)).place(x = 350, y = 200)
var_gender.set("male")

check_ = Checkbutton(root, variable = var_check, text = "Accept our Terms and Conditions", onvalue = 1, offvalue = 0, font = ("times new roman", 13)).place(x = 250, y = 280)

btn = Button(root, text = "Show Data", command = get_data, font = ("times new roman", 20, "bold"), bg = "gray", fg = "white").place(x = 300, y = 320, width = 150, height = 30)

lbl_result = Label(root, text = "", font = ("times new roman", 15))
lbl_result.place(x = 0, y = 380, relwidth = 1)

root.mainloop()