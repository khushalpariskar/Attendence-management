from tkinter import *
#from dashboard import *
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=datetime.date.today()
#print(t)
#root=Tk()
#root.geometry('1350x700+0+0')

root=Frame(bg='white')
root.place(x=0,y=0,height=800,width=1350)


t=datetime.date.today()

#------------------


#=-----------------
frm=Frame(root,bg='green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm.place(x=10,y=10)
Label(root,text='ATTENDENCE MANAGEMENT',bg='green',font=('calibri',13,'bold')).place(x=605,y=15)
import datetime

import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')


def select():
    manage_frame = Frame(root, bd=4, relief=RIDGE, bg="green")
    manage_frame.place(x=170, y=100, width=1000, height=500)

    min_frm=Frame(manage_frame, bd=4, relief=RIDGE, bg="green")
    min_frm.place(x=200,y=100,width=600,height=300)

    t=tdy_day.get()+'_tch'

    print(t)
    sql_cmd="select * from "+str(t)+""
    #sql_cmd_2="select section from "+str(t)+""
    mycursor.execute(sql_cmd)
    t=mycursor.fetchall()
    #mycursor.execute(sql_cmd_2)
    #s=mycursor.fetchall()
    x=0
    for i in t:
        x+=1
        #print('t[]',t[i])
        Label(min_frm,text=i,fg='black',height=3,width=90).place(x=0,y=50*x)
        #Label(min_frm,text=s[i],height=50,width=200).place(x=500,y=10)


manage_frame = Frame(root, bd=4, relief=RIDGE, bg="green")
manage_frame.place(x=170, y=100, width=1000, height=500)
day = StringVar()
lbl = Label(manage_frame, text="SELECT RESPECTIVE DAY:-", font=('calibri', 13))
lbl.place(x=290,y=130,width=370,height=50)
tdy_day = ttk.Combobox(manage_frame, font=('calibri', 13), textvariable=day)
tdy_day['values'] = ("Monday", "Tuesday", "Wednesday","Thrusday","Friday","Saturday","Sunday")
tdy_day.place(x=290,y=200,width=370,height=50)


Button(manage_frame,text='Proceed',command=lambda :select()).place(x=330,y=300,width=300,height=50)


















root.mainloop()