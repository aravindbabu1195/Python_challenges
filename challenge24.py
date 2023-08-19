from tkinter import *
root=Tk()
frame1=Frame(root)
frame1.pack()

def new1():
    print("New Project")

def new2():
    print("New ")

def new3():
    print("New Scratch")

def new4():
    print("Open")

def new5():
    print("Save As")

def new6():
    print("Open Recent")

def edit1():
    print("Undo Typing")

def edit2():
    print("Redo")

def edit3():
    print("Cut")

def edit4():
    print("Copy")

def edit5():
    print("Paste")

def edit6():
    print("Delete")












filemenu=Menu(frame1)
root.config(menu=filemenu)

submenu=Menu(filemenu)
filemenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project",command=new1)
submenu.add_command(label="New",command=new2)
submenu.add_separator()
submenu.add_command(label="New Scrach File",command=new3)
submenu.add_command(label="Open",command=new4)
submenu.add_separator()
submenu.add_command(label="Save As",command=new5)
submenu.add_command(label="Open Recent",command=new6)
submenu.add_command(label="Exit",command=frame1.quit)

editmenu=Menu(filemenu)
filemenu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",command=edit1)
editmenu.add_command(label="Redo",command=edit2)
editmenu.add_separator()
editmenu.add_command(label="Cut",command=edit3)
editmenu.add_command(label="Copy",command=edit4)
editmenu.add_separator()
editmenu.add_command(label="Paste",command=edit5)
editmenu.add_command(label="Delete",command=edit6)

viewmenu=Menu(filemenu)
filemenu.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Tool Window")
viewmenu.add_command(label="Appearance")
viewmenu.add_separator()
viewmenu.add_command(label="Quick Definition")
viewmenu.add_command(label="Quick Type Definition")
viewmenu.add_separator()
viewmenu.add_command(label="Quick Documentation")
viewmenu.add_command(label="Parameter Info")

navigatemenu=Menu(filemenu)
filemenu.add_cascade(label="Navigate",menu=navigatemenu)
navigatemenu.add_command(label="Back")
navigatemenu.add_command(label="Forward")
navigatemenu.add_separator()
navigatemenu.add_command(label="Search Everywhere")
navigatemenu.add_command(label="Class")
navigatemenu.add_separator()
navigatemenu.add_command(label="File")
navigatemenu.add_command(label="Symbol")

codemenu=Menu(filemenu)
filemenu.add_cascade(label="Code",menu=codemenu)
codemenu.add_command(label="Override Methods")
codemenu.add_command(label="Implement Methods")
codemenu.add_separator()
codemenu.add_command(label="Generate")
codemenu.add_command(label="Code Completion")
codemenu.add_separator()
codemenu.add_command(label="Insert Live_Template")
codemenu.add_command(label="Surround With")

toolbar=Frame(root,bg="pink")
inbutton=Button(toolbar,text="Refresh")
inbutton.pack(side=LEFT,padx=4,pady=2)
toolbar.pack(side=TOP,fill=X)

statusbar=Label(root,text="Footer",bd=5,bg="aqua",relief=SUNKEN)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
