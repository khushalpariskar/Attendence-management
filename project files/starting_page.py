from tkinter import *
root=Tk()
root.geometry('1350x750+0+0')
root.title('ATTENDENCE MANAGEMENT1')
def here():
    import login_signing
Button(root,text='start',command=here,height=2,width=50,bg='green').place(x=500,y=250)
root.mainloop()