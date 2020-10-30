from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#root=Tk()
#root.geometry('1350x750+0+0')
root=Frame(bg='white')
root.place(x=0,y=0,height=750,width=1380)
Label(root,text='UPDATE CLASSES', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()


import datetime

import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')



def update():
    t=tdy_day.get()
    tab=str(t)+'_tch'
    manage_frame = Frame(root, bd=4)
    manage_frame.place(x=170, y=50, width=1000, height=600)


    Label(root,text='ADD CLASS',height=2,width=40,bg='green').place(x=170,y=510)
    upd = Frame(root, bd=4, bg='green')
    upd.place(x=170, y=550, width=1000, height=50)


    def save():
        sql_cmd="insert into "+str(tab)+" values('"+ety1.get()+"','"+ety2.get()+"')"
        mycursor.execute(sql_cmd)
        mycursor.execute("commit")
        update()
        print(ety1.get())
        print(ety2.get())

    Label(upd,text='Enter Section',height=2,width=25,bg='white').place(x=0,y=0)
    ety1=Entry(upd)
    ety1.place(x=200,y=0,height=37,width=100)

    Label(upd,text='Enter Timing',height=2,width=25,bg='white').place(x=400,y=0)
    ety2=Entry(upd)
    ety2.place(x=600,y=0,height=37,width=100)

    Button(upd,height=2,width=25,text='Proceed',command=lambda :save()).place(x=800,y=0)


    print('str(tab)',str(tab))
    sql_cmd_date="select time from "+str(tab)+""
    mycursor.execute(sql_cmd_date)
    d_time = mycursor.fetchall()
    num=len(d_time)
    sql_cmd_cls = "select section from "+str(tab)+""
    mycursor.execute(sql_cmd_cls)
    d_class=mycursor.fetchall()

    classes=Frame(manage_frame,bg='green',width=680,height=400)

    classes.place(x=150,y=20)


    def upd_data(t1):

        def proceed():

            def proceed1(val):
                print('val:',val)
                print('t1',t1)
                sql_cmd_upd="update "+str(tab)+"set timing='"+val+"' where section='"+t1+"';"
                mycursor.execute(sql_cmd_upd)
                #update()



            val=StringVar()
            Label(root, text='UPDATE CLASS', height=2, width=40, bg='green').place(x=170, y=620)
            upd = Frame(root, bd=4, bg='green')
            upd.place(x=170, y=660, width=1000, height=50)
            Label(upd, text='ENTER NEW TIME:-', padx=5, pady=10).place(x=10, y=10, height=30, width=130)
            ety1=Entry(upd,textvariable=val)
            ety1.place(x=200, y=10, height=30, width=300)
            xys=str(ety1.get())
            print('val*=',xys)
            Button(upd, text='proceed',command=proceed1(xys)).place(x=600, y=10, height=30, width=100)





        Label(root, text='UPDATE CLASS', height=2, width=40, bg='green').place(x=170, y=620)
        upd = Frame(root, bd=4, bg='green')
        upd.place(x=170, y=660, width=1000, height=50)
        proceed()
        """
        Label(upd,text='SECTION:-',padx=5,pady=10).place(x=10,y=10,height=30,width=100)
        Entry(upd).place(x=200,y=10,height=30,width=300)
        Button(upd,text='proceed',command=proceed).place(x=600,y=10,height=30,width=100)
        """



    def dlt_cls(t1):
        print('dlt t1',t1)
        sql_cmd_upd = "delete from  "+str(tab)+" where section='"+t1+"'"
        mycursor.execute(sql_cmd_upd)
        mycursor.execute("commit")
        messagebox.askokcancel('yeah','deleted succesfully')
        update()
    for i in range(1,num):
        t1=d_class[i][0]
        t2=d_time[i][0]

        Label(classes,text='STARTING TIMING',padx=10,pady=10,height=1,width=15, font=('calibri', 10, 'bold')).place(x=50,y=0)
        Label(classes,text='SECTION',padx=10,pady=10,height=1,width=15, font=('calibri', 10, 'bold')).place(x=180,y=0)
        Label(classes,text=t2,padx=10,pady=10,height=1,width=15, font=('calibri', 10, 'bold')).place(x=50,y=50*i)
        Label(classes,text=t1,padx=10,pady=10,height=1,width=15, font=('calibri', 10, 'bold')).place(x=180,y=50*i)
        Button(classes,text='DELETE',padx=10,pady=10,width=40, font=('calibri', 10, 'bold'),command=lambda :dlt_cls(t1)).place(x=310,y=50*i,height=40)
        #Button(classes,text='UPDATE',padx=10,pady=10,width=15, font=('calibri', 10, 'bold'),command=lambda :upd_data(t1)).place(x=448,y=50*i,height=40)




manage_frame = Frame(root, bd=4, relief=RIDGE, bg="green")
manage_frame.place(x=170, y=100, width=1000, height=500)

day = StringVar()
lbl = Label(manage_frame, text="SELECT RESPECTIVE DAY:-", font=('calibri', 13))
lbl.place(x=290,y=130,width=370,height=50)
tdy_day = ttk.Combobox(manage_frame, font=('calibri', 13), textvariable=day)
tdy_day['values'] = ("Monday", "Tuesday", "Wednesday","Thrusday","Friday","Saturday","Sunday")
tdy_day.place(x=290,y=200,width=370,height=50)


Button(manage_frame,text='Proceed',command=lambda :update()).place(x=330,y=300,width=300,height=50)

root.mainloop()