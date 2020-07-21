from tkinter import *


root = Tk()
root.title("GUI Layout")
root.geometry("800x500+250+50")

def get_language():
    get_cursor = language_list.curselection()
    #print(get_cursor)
    #print(language_list.get(0))
    #for i in get_cursor:
    #    print(language_list.get(i))
    language_list.delete(get_cursor)


language_list = Listbox(root, font = ("times new roman", 15), bg = "#262626", fg = "white", justify = CENTER, selectmode = BROWSE)
language_list.place(x = 100, y = 50, width = 150)

for i in range(20):
    language_list.insert(i, "Language: "+ str(i))

btn = Button(root, command = get_language, text = "SHOW", font = ("times new roman", 20), bg = "green", fg = "white").place(x = 120, y = 300, height = 30)





root.mainloop()