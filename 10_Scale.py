from tkinter import *
root = Tk()
root.title("GUI Layout")
root.geometry("800x500+250+50")
root.config(bg = "#262626")

def get_price(price_):
    lbl_result.config(text = str(price_))

price = Scale(root, from_ = 50, to = 250, orient = HORIZONTAL, sliderlength = 100,length = 700, showvalue = FALSE, command = get_price)
price.place(x = 50, y = 50, width = 700)

lbl_result = Label(root, bg = "#262626", fg = "white")
lbl_result.place(x = 0, y = 100, relwidth = 1)




root.mainloop()