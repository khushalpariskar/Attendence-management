from tkinter import *
#from dashboard import *
import datetime
t=datetime.date.today()
#print(t)
#root=Tk()
#root.geometry('1350x700+0+0')

root=Frame(bg='white')
root.place(x=0,y=0,height=800,width=1350)

import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')



t=datetime.date.today()

#------------------


#=-----------------
frm=Frame(root,bg='green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm.place(x=10,y=10)
Label(root,text='ATTENDENCE MANAGEMENT',bg='green',font=('calibri',13,'bold')).place(x=605,y=15)

frm1=Frame(root,bg='light green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm1.place(x=10,y=70)
Label(root,text=datetime.date.today(),bg='light green',font=('calibri',13,'bold')).place(x=20,y=75)
#--------------

main_frm=Frame(root,bg='green',height=500,width=1320,relief=GROOVE,padx=50,pady=30)
main_frm.place(x=10,y=150)

frame=Label(root,bg='blue',text='UPCOMING',font=('calibri',13,'bold')).place(x=1080,y=75,height=29,width=100)
frame=Label(root,bg='red',text='ONGOINING',font=('calibri',13,'bold')).place(x=1200,y=75,height=29,width=100)
frame=Label(root,bg='grey',text='COMPLETED',font=('calibri',13,'bold')).place(x=960,y=75,height=29,width=100)



def tdy_cls(cls,time1,i):
    t_now=datetime.datetime.now()
    t_now1=t_now.hour
    if t_now1==time1:
        color='red'
        txt1='ATTEND'
        txt2='APPLY LEAVE'
        cmd_btn1='attend_class'
        cmd_btn2='leave_application'
    elif t_now1>time1:
        color='grey'
        f=open("regno_pswd.txt","r")
        t=f.read()
        f11=open("class.txt","r")
        t11=f11.read()
        print('t22',str(t11))
        sql_cmd="select status1 from "+str(t11)+" where regno="+str(t)+""
        mycursor.execute(sql_cmd)
        t=mycursor.fetchone()



        txt1=t
        txt2='VIEW ATTENDENCE'
    elif t_now1<time1:
        color='blue'
        txt1='SET REMINDER'
        txt2='APPLY LEAVE'


    def fun(txt1,cls,time1):
        if txt1=='ATTEND':
            attend_class1()

        elif txt1=='STATUS':
            pass
            #print('status')

        elif txt1=='SET REMINDER':
            reminder(cls,time1)
            #print('reminder')


    def attend_class1():
        import atd_cal1
        f=open("regno_pswd.txt","r")
        t=f.read()
        t_now_a = datetime.datetime.now()
        t_now1_a = t_now_a.hour
        #print('cls',cls)
        f=open("class.txt","w")
        f.write(cls)
        date=datetime.date.today()
        #print(date)
        #print(date)
        print('str(cls)',str(cls))


        sql_cmd="insert into "+str(cls)+" values('"+str(t)+"','"+str(t_now1_a)+"','A','"+str(date)+"')"
        mycursor.execute(sql_cmd)
        mycursor.execute("commit")



    def leave_application():
        import leave

    time= datetime.time(time1 + 1, 0, 0, 0)
    scd_frm = Frame(main_frm, bg=color, height=50, width=1220, relief=GROOVE, padx=5, pady=5)
    scd_frm.place(x=00, y=i * 60)
    Label(scd_frm, text=datetime.time(time1, 0, 0, 0), padx=1, pady=1, bg=color,font=('calibri', 13, 'bold')).place(x=1, y=0, width=100, height=50)
    Label(scd_frm, text=datetime.time(time1+1, 0, 0, 0), padx=1, pady=1, bg=color,font=('calibri', 13, 'bold')).place(x=110, y=0, width=100, height=50)
    Label(scd_frm, text=cls, padx=1, pady=1, bg=color, font=('calibri', 13, 'bold')).place(x=400, y=0,width=100,height=50)
    Button(scd_frm, text=txt1, padx=50, pady=30, bg='white', font=('calibri', 13),command=lambda:fun(txt1,cls,time1)).place(x=750, y=0,width=200,height=45)
    Button(scd_frm, text=txt2, padx=50, pady=30, bg='white', font=('calibri', 13),command=leave_application).place(x=1000, y=0,width=200,height=45)


    def reminder(cls,time1):
        scd_frm=Frame(root,bg='blue',width=1100,height=50)
        scd_frm.place(x=50,y=670)
        Label(scd_frm, text=datetime.time(time1, 0, 0, 0), padx=1, pady=1, bg=color,font=('calibri', 13, 'bold')).place(x=1, y=0, width=100, height=50)
        Label(scd_frm, text=datetime.time(time1+1, 0, 0, 0), padx=1, pady=1, bg=color,font=('calibri', 13, 'bold')).place(x=110, y=0, width=100, height=50)
        Label(scd_frm, text=cls, padx=1, pady=1, bg=color, font=('calibri', 13, 'bold')).place(x=400, y=0,width=100,height=50)
        Button(scd_frm, text='APPLY LEAVE', padx=50, pady=30, bg='white', font=('calibri', 13),command=leave_application).place(x=750, y=0,width=200,height=45)




def sel_tdy_cls():

    sql_cmd_date="select starting_time from Mondey_engineering"
    mycursor.execute(sql_cmd_date)
    d_time=mycursor.fetchall()
    num=len(d_time)
    sql_cmd_cls="select class from Mondey_engineering"
    mycursor.execute(sql_cmd_cls)
    d_class=mycursor.fetchall()
    #print(d_class)
    for i in range(num):
        p=d_time[i][0]
        tm1=datetime.time(p, 0, 0, 0)
        tm2=datetime.time(p+1, 0, 0, 0)
        p_c=d_class[i][0]
        tdy_cls(p_c,p,i)
    print('d_class',d_class)







sel_tdy_cls()
Label(frm, text='')
root.mainloop()
