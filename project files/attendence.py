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

left_frm=Frame(root,height=600,width=650,bg='green')
left_frm.place(x=0,y=80)

right_frm=Frame(root,height=600,width=650,bg='green')
right_frm.place(x=700,y=80)


def side(a):
    right_frm = Frame(root, height=600, width=650, bg='green')
    right_frm.place(x=700, y=80)
    print('a',a[0])
    sql_cmd="select date,timing,status1 from "+str(a[0])+""
    mycursor.execute(sql_cmd)
    t = mycursor.fetchall()
    l = len(t)
    for i in range(0, l):
        Label(right_frm, text=t[i], height=2, width=80).place(x=20, y=50 * i + 10)


sql_cmd="select class from mondey_engineering"
mycursor.execute(sql_cmd)
t=mycursor.fetchall()
l=len(t)

def frm(a):
    lb_frm=Label(left_frm,bg='green',height=4,width=90)
    lb_frm.pack()
    lbl=Label(lb_frm,text=a,height=2,width=40)
    lbl.place(x=20,y=10)
    Button(lb_frm,text='DETAILS',height=2,width=30,command=lambda:side(a)).place(x=350,y=10)



for i in range(0,l):

    a=t[i]
    frm(a)










root.mainloop()