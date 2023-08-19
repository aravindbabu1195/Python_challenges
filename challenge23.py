from tkinter import *
class action:
    def __init__(self,root):
        frame=Frame(root)
        self.label1=Label(frame,text="Click here")
        self.label2=Label(frame,text="Cancel here")
        self.label3=Label(frame,text="Exit here")
        self.pbutton=Button(frame,text="Clik",command=self.msg)
        self.cbutton = Button(frame, text="Cancel",command=self.msg1)
        self.qbutton = Button(frame, text="Clik",command=frame.quit)

        frame.grid()
        self.label1.grid(row=0,column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.pbutton.grid(row=0, column=1)
        self.cbutton.grid(row=1, column=1)
        self.qbutton.grid(row=2, column=1)
    def msg(self):
        print("Cliked")

    def msg1(self):
        print("Canceled")

root=Tk()
obj=action(root)
root.mainloop()