from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#root=Tk()
#root.geometry('1350x750+0+0')
root=Frame(bg='white')
root.place(x=0,y=0,height=750,width=1380)
Label(root,text='STUDENT INFORMATION', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()

import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')


manage_frame = Frame(root, bd=4, relief=RIDGE, bg="green")
manage_frame.place(x=170, y=100, width=1000, height=500)

day = StringVar()
lbl = Label(manage_frame, text="SELECT RESPECTIVE SECTION:-", font=('calibri', 13))
lbl.place(x=600,y=130,width=370,height=50)
tdy_day = ttk.Combobox(manage_frame, font=('calibri', 13), textvariable=day)
tdy_day['values'] = ("A", "B", "C","D","E")
tdy_day.place(x=600,y=200,width=370,height=50)

day = StringVar()
lbl = Label(manage_frame, text="SELECT RESPECTIVE DAY:-", font=('calibri', 13))
lbl.place(x=10,y=130,width=370,height=50)
tdy_day = ttk.Combobox(manage_frame, font=('calibri', 13), textvariable=day)
tdy_day['values'] = ("Mondey", "Tuesday", "Wednesday","Thrusday","Friday","Saturday","Sunday")
tdy_day.place(x=10,y=200,width=370,height=50)



def second_frame():
    main_frm=Frame(root,bg='white')
    main_frm.place(x=0,y=70,height=650,width=1350)

    left_frm=Frame(main_frm,bg='green')
    left_frm.place(x=10,y=50,height=720,width=650)

    Label(left_frm,text='TOTAL STUDENT').place(x=0,y=10,height=50,width=650)


    left_center_frm=Frame(left_frm,bg='white')
    left_center_frm.place(x=23,y=90,height=400,width=600)

    sql_cmd="select * from student"
    mycursor.execute(sql_cmd)
    ftch=mycursor.fetchall()
    n=len(ftch)

    for i in ftch:
        Label(left_center_frm,text=i).pack()



    right_up_frm=Frame(main_frm,bg='green')
    right_up_frm.place(x=690,y=50,height=290,width=650)

    Label(right_up_frm,text='STUDENT PRESENT').place(x=0,y=10,height=50,width=650)

    f=open('regno_pswd.txt','r')
    reg=f.read()


    sql_cmd_present="select regno from attendence where status1='P'"
    mycursor.execute(sql_cmd_present)
    t=mycursor.fetchall()

    for i in t:
        print(i[0])
        sql_cmd_present = "select * from student where regno='"+str(i[0])+"'"
        mycursor.execute(sql_cmd_present)
        t = mycursor.fetchone()

        min_frm=Frame(right_up_frm,bg='black',height=100,width=500)
        min_frm.place(x=60,y=100)
        Label(min_frm,text=t).pack()






    right_down_frm=Frame(main_frm,bg='green')
    right_down_frm.place(x=690,y=350,height=290,width=650)

    Label(right_down_frm,text='STUDENT ABSENT').place(x=0,y=10,height=50,width=650)

    sql_cmd_present="select regno from attendence where status1='A'"
    mycursor.execute(sql_cmd_present)
    t=mycursor.fetchall()


    for i in t:
        print(i[0])
        sql_cmd_present = "select * from student where regno='"+str(i[0])+"'"
        mycursor.execute(sql_cmd_present)
        t = mycursor.fetchone()

        min_frm=Frame(right_down_frm,bg='black',height=100,width=500)
        min_frm.place(x=60,y=100)
        Label(min_frm,text=t).pack()





Button(manage_frame,text='Proceed',command=second_frame).place(x=330,y=300,width=300,height=50)





root.mainloop()