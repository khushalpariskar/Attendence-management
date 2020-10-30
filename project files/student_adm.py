from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#root=Tk()
#root.geometry('1350x750+0+0')
root=Frame(bg='white')
root.place(x=0,y=0,height=750,width=1380)
Label(root,text='STUDENT INFORMATION', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()


import datetime

import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')



main_frm=Frame(root,bg='green',height=600,width=1000)
main_frm.place(x=150,y=100)


def updt(a):
    print(a)

    def name():
        frm1=Frame(main_frm,bg='green',height=300,width=1000)
        frm1.place(x=200,y=150)

        print('a[]',a[0])
        sql_cmd="select name from student where regno='"+str(a[0])+"'"
        mycursor.execute(sql_cmd)
        lbl=mycursor.fetchone()
        old_lbl=Label(frm1,text='OLD DATA:-',height=2,width=50)
        old_lbl.place(x=20,y=20)
        print('lbl',lbl)
        Label(frm1,text=lbl,height=2,width=50).place(x=400,y=20)
        new_lbl = Label(frm1, text='ENTER NEW DATA:-', height=2, width=50)
        new_lbl.place(x=20, y=80)
        print('lbl', lbl)
        ety=Entry(frm1)
        ety.place(x=400, y=80, height=40, width=360)

        def save(val):
            sql_cmd = "update student set name='"+str(val)+"' where regno='"+str(a)+"';"
            mycursor.execute(sql_cmd)
            mycursor.execute("commit")



        Button(frm1,text='SAVE DATA',bg='blue',command=lambda :save(ety.get())).place(x=200, y=180, height=40, width=360)





    def regno():
        frm1=Frame(main_frm,bg='green',height=300,width=1000)
        frm1.place(x=200,y=150)

        print('a[]',a[0])
        sql_cmd="select regno from student where regno='"+str(a[0])+"'"
        mycursor.execute(sql_cmd)
        lbl=mycursor.fetchone()
        old_lbl=Label(frm1,text='OLD DATA:-',height=2,width=50)
        old_lbl.place(x=20,y=20)
        print('lbl',lbl)
        Label(frm1,text=lbl,height=2,width=50).place(x=400,y=20)
        new_lbl = Label(frm1, text='ENTER NEW DATA:-', height=2, width=50)
        new_lbl.place(x=20, y=80)
        print('lbl', lbl)
        ety=Entry(frm1)
        ety.place(x=400, y=80, height=40, width=360)

        def save(val):
            sql_cmd = "update student set regno='"+str(val)+"' where regno='"+str(a)+"';"
            mycursor.execute(sql_cmd)
            mycursor.execute("commit")



        Button(frm1,text='SAVE DATA',bg='blue',command=lambda :save(ety.get())).place(x=200, y=180, height=40, width=360)






    def phn():
        frm1=Frame(main_frm,bg='green',height=300,width=1000)
        frm1.place(x=200,y=150)

        print('a[]',a[0])
        sql_cmd="select contact_number from student where regno='"+str(a[0])+"'"
        mycursor.execute(sql_cmd)
        lbl=mycursor.fetchone()
        old_lbl=Label(frm1,text='OLD DATA:-',height=2,width=50)
        old_lbl.place(x=20,y=20)
        print('lbl',lbl)
        Label(frm1,text=lbl,height=2,width=50).place(x=400,y=20)
        new_lbl = Label(frm1, text='ENTER NEW DATA:-', height=2, width=50)
        new_lbl.place(x=20, y=80)
        print('lbl', lbl)
        ety=Entry(frm1)
        ety.place(x=400, y=80, height=40, width=360)

        def save(val):
            sql_cmd = "update student set contact_number='"+str(val)+"' where regno='"+str(a)+"';"
            mycursor.execute(sql_cmd)
            mycursor.execute("commit")



        Button(frm1,text='SAVE DATA',bg='blue',command=lambda :save(ety.get())).place(x=200, y=180, height=40, width=360)



    def email():
        frm1=Frame(main_frm,bg='green',height=300,width=1000)
        frm1.place(x=200,y=150)

        print('a[]',a[0])
        sql_cmd="select email from student where regno='"+str(a[0])+"'"
        mycursor.execute(sql_cmd)
        lbl=mycursor.fetchone()
        old_lbl=Label(frm1,text='OLD DATA:-',height=2,width=50)
        old_lbl.place(x=20,y=20)
        print('lbl',lbl)
        Label(frm1,text=lbl,height=2,width=50).place(x=400,y=20)
        new_lbl = Label(frm1, text='ENTER NEW DATA:-', height=2, width=50)
        new_lbl.place(x=20, y=80)
        print('lbl', lbl)
        ety=Entry(frm1)
        ety.place(x=400, y=80, height=40, width=360)

        def save(val):
            sql_cmd = "update student set email='"+str(val)+"' where regno='"+str(a)+"';"
            mycursor.execute(sql_cmd)
            mycursor.execute("commit")



        Button(frm1,text='SAVE DATA',bg='blue',command=lambda :save(ety.get())).place(x=200, y=180, height=40, width=360)





    def adr():
        frm1=Frame(main_frm,bg='green',height=300,width=1000)
        frm1.place(x=200,y=150)

        print('a[]',a[0])
        sql_cmd="select permanent_address from student where regno='"+str(a[0])+"'"
        mycursor.execute(sql_cmd)
        lbl=mycursor.fetchone()
        old_lbl=Label(frm1,text='OLD DATA:-',height=2,width=50)
        old_lbl.place(x=20,y=20)
        print('lbl',lbl)
        Label(frm1,text=lbl,height=2,width=50).place(x=400,y=20)
        new_lbl = Label(frm1, text='ENTER NEW DATA:-', height=2, width=50)
        new_lbl.place(x=20, y=80)
        print('lbl', lbl)
        ety=Entry(frm1)
        ety.place(x=400, y=80, height=40, width=360)

        def save(val):
            sql_cmd = "update student set permanent_address='"+str(val)+"' where regno='"+str(a)+"';"
            mycursor.execute(sql_cmd)
            mycursor.execute("commit")



        Button(frm1,text='SAVE DATA',bg='blue',command=lambda :save(ety.get())).place(x=200, y=180, height=40, width=360)







    def psd():
        frm1=Frame(main_frm,bg='green',height=300,width=1000)
        frm1.place(x=200,y=150)

        print('a[]',a[0])
        sql_cmd="select password from student where regno='"+str(a[0])+"'"
        mycursor.execute(sql_cmd)
        lbl=mycursor.fetchone()
        old_lbl=Label(frm1,text='OLD DATA:-',height=2,width=50)
        old_lbl.place(x=20,y=20)
        print('lbl',lbl)
        Label(frm1,text=lbl,height=2,width=50).place(x=400,y=20)
        new_lbl = Label(frm1, text='ENTER NEW DATA:-', height=2, width=50)
        new_lbl.place(x=20, y=80)
        print('lbl', lbl)
        ety=Entry(frm1)
        ety.place(x=400, y=80, height=40, width=360)

        def save(val):
            sql_cmd = "update student set password='"+str(val)+"' where regno='"+str(a)+"';"
            mycursor.execute(sql_cmd)
            mycursor.execute("commit")



        Button(frm1,text='SAVE DATA',bg='blue',command=lambda :save(ety.get())).place(x=200, y=180, height=40, width=360)






    main_frm = Frame(root, bg='green', height=527, width=1050)
    main_frm.place(x=150, y=100)

    mini_frm=Frame(main_frm, bg='white', height=50, width=1100)
    mini_frm.place(x=100,y=50)

    Button(mini_frm,text='NAME',height=3,width=20,command=lambda:name()).pack(side=LEFT)
    Button(mini_frm,text='REGNO',height=3,width=20,command=lambda:regno()).pack(side=LEFT)
    Button(mini_frm,text='PHONE number',height=3,width=30,command=lambda:phn()).pack(side=LEFT)
    Button(mini_frm,text='EMAIL',height=3,width=20,command=lambda:email()).pack(side=LEFT)
    Button(mini_frm,text='ADDRESS',height=3,width=20,command=lambda:adr()).pack(side=LEFT)
    Button(mini_frm,text='PASSWORD',height=3,width=20,command=lambda:psd()).pack(side=LEFT)


def dlt(t1):
    print('dlt t1', t1)
    sql_cmd_upd = "delete from  student_acd where reg_no='" + t1[0] + "'"
    mycursor.execute(sql_cmd_upd)
    mycursor.execute("commit")

    sql_cmd_upd = "delete from  student where regno='" + t1[0] + "'"
    mycursor.execute(sql_cmd_upd)
    mycursor.execute("commit")
    messagebox.askokcancel('yeah', 'deleted succesfully refresh program to see the change')






def frm(a):
    lb_frm=Label(main_frm,bg='green',height=4,width=149)
    lb_frm.pack()
    lbl=Label(lb_frm,text=a,height=2,width=40,bg='white')
    lbl.place(x=20,y=10)
    print(a)
    sql_cmd1="select name from student where regno='"+str(a[0])+"'"
    mycursor.execute(sql_cmd1)
    n=mycursor.fetchone()
    Label(lb_frm,text=n,height=2,width=40,bg='white').place(x=300,y=10)
    btn=Button(lb_frm,text='UPDATE USER',bg='blue',height=2,width=30,command=lambda:updt(a[0]))
    btn.place(x=600,y=10)
    btn=Button(lb_frm,text='DELETE USER',bg='red',height=2,width=30,command=lambda :dlt(a[0]))
    btn.place(x=800,y=10)
    #Button(lb_frm,text='DELETE',height=30,width=30).place(x=700,y=10)


sql_cmd="select regno from student"
mycursor.execute(sql_cmd)
t=mycursor.fetchall()



for i in range(0,len(t)):

    a=t[i]
    frm(a)





root.mainloop()