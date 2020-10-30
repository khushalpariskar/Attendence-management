from tkinter import *
from tkinter import messagebox
import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor()
print(stud)
if(stud):
    print('successful')

#root=Tk()
#root.title('TIME_TABLE')
#root.geometry("1350x700+0+0")


root=Frame(bg='white')
root.place(x=0,y=0,height=800,width=1350)



frm=Frame(root,bg='green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm.place(x=10,y=10)
Label(root,text='ATTENDENCE MANAGEMENT',bg='green',font=('calibri',13,'bold')).place(x=570,y=15)


frm2=Frame(root,bg='green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm2.place(x=10,y=80)
Label(root,text='APPLY FOR LEAVE',bg='green',font=('calibri',13,'bold')).place(x=605,y=85)


main_frm=Frame(root,bg='green',height=500,width=1320,relief=GROOVE,padx=50,pady=30)
main_frm.place(x=10,y=150)


sub_frm=Frame(main_frm,bg='white',height=450,width=400,relief=GROOVE,padx=10,pady=10)
sub_frm.place(x=430,y=10)


def btn11():
    messagebox.askokcancel(title='SAVED ', message='DATA SAVED SUCCESSFULLY')
    num=reg.get()
    print(num)
    sql_cmd="update attendence set status1='L' where regno ='"+num+"'"
    mycursor.execute(sql_cmd)
    mycursor.execute("commit")






Label(sub_frm,text='APPLY FOR LEAVE',font=('calibri',13,'bold')).place(x=100,y=0)
Label(sub_frm,text='NAME',font=('calibri',13,'bold')).place(x=0,y=50)
Entry(sub_frm,text='APPLY FOR LEAVE',font=('calibri',13,'bold')).place(x=200,y=50)
Label(sub_frm,text='REGISTRATION NUMBER',font=('calibri',13,'bold')).place(x=0,y=90)
reg=Entry(sub_frm,text='REGISTRATION NUMBER',font=('calibri',13,'bold'))
reg.place(x=200,y=90)
Label(sub_frm,text='PASSWORD',font=('calibri',13,'bold')).place(x=0,y=130)
Entry(sub_frm,font=('calibri',13,'bold')).place(x=200,y=130)
Label(sub_frm,text='DATE OF BIRTH',font=('calibri',13,'bold')).place(x=0,y=175)
Entry(sub_frm,font=('calibri',13,'bold')).place(x=200,y=170)
Label(sub_frm,text='pls state your REASON',font=('calibri',13,'bold')).place(x=0,y=220)
Entry(sub_frm,text='REASON',bg='light grey',font=('calibri',13,'bold')).place(x=10,y=270,width=350,height=80)
Button(sub_frm,text='SUBMIT',bg='light grey',font=('calibri',13,'bold'),command=btn11).place(x=10,y=370,width=350,height=60)



#root.mainloop()