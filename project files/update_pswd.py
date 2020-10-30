from tkinter import *
from tkinter import ttk
import tkcalendar
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor()
print(stud)
if(stud):
    print('successful')

root=Frame()
root.place(x=0,y=0,height=800,width=1400)

Label(root,text='ATTENDENCE MANAGEMENT', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()





def new_old():

    def upd():
        if(oety1.get()==oety2.get()):
            print('entered')
            sql_cmd="update student set password='"+str(oety1.get())+"' where regno='"+str(ety1.get())+"';"
            mycursor.execute(sql_cmd)
            messagebox.askokcancel('updated','password updated successfully')
            mycursor.execute('commit')
        else:
            messagebox.askretrycancel('ERROR','password DOESNOT MATCH')


    center = Frame(root, bg='green', width=500, height=350)
    center.place(x=450, y=180)
    Label(center, text='ENTER PASSWORD', width=30, height=3).place(x=20, y=40)
    oety1 = Entry(center)
    oety1.place(x=280, y=48,height=25,width=180)

    Label(center, text='VERIFY PASSWORD', width=30, height=3).place(x=20, y=130)
    oety2 = Entry(center)
    oety2.place(x=280, y=138,height=25,width=180)

    Button(center, text='PROCEED', width=50, height=3,command=lambda:upd()).place(x=70, y=250)


def pro1():
    sql_reg="select password from student where regno='"+str(ety1.get())+"' "
    mycursor.execute(sql_reg)
    psd=mycursor.fetchone()
    if(psd[0]==ety2.get()):
        new_old()
    else:
        messagebox.askretrycancel('ERROR','WRONG ID OR PASSWORD')




center = Frame(root, bg='green', width=500, height=350)
center.place(x=450, y=180)
Label(center, text='REGISTRATION NUMBER', width=30, height=3).place(x=20, y=40)
ety1 = Entry(center)
ety1.place(x=280, y=48, height=25, width=180)

Label(center, text='OLD PASSWORD', width=30, height=3).place(x=20, y=130)
ety2 = Entry(center)
ety2.place(x=280, y=138, height=25, width=180)

Button(center, text='PROCEED*', width=50, height=3,command=lambda:pro1()).place(x=70, y=250)


root.mainloop()