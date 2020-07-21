from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI Layout")
root.geometry("800x500+250+50")
root.config(bg = "#262626")

def employeeDetails():
    messagebox.showinfo("EmployeeMenu", "This is employee menu bar")

MyMenu = Menu(root)
#MyMenu.add_command(label = "Employee",command=employeeDetails)
#MyMenu.add_command(label = "Employee",command=employeeDetails)
DetailsMenu = Menu(MyMenu, tearoff = 0)
DetailsMenu.add_command(label = "Managers Details")
DetailsMenu.add_command(label = "Employee Details")


EmployeeMenu = Menu(MyMenu, tearoff = 0)
EmployeeMenu.add_command(label = "Add Employee",command=employeeDetails)
EmployeeMenu.add_command(label = "Delete Employee",command=employeeDetails)
EmployeeMenu.add_cascade(label = "View Employee",menu = DetailsMenu)
EmployeeMenu.add_separator()
EmployeeMenu.add_command(label = "Exit",command=employeeDetails)


DepartmentMenu = Menu(MyMenu, tearoff = 0)
DepartmentMenu.add_command(label = "Add ",command=employeeDetails)
DepartmentMenu.add_command(label = "Delete ",command=employeeDetails)
DepartmentMenu.add_command(label = "View ",command=employeeDetails)


MyMenu.add_cascade(label = "Employee", menu = EmployeeMenu)
MyMenu.add_cascade(label = "Department", menu = DepartmentMenu)

root.config(menu=MyMenu)




root.mainloop()