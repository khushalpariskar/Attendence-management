from tkinter import *
from datetime import datetime
from tkinter import messagebox as mb
#from datetime import time
import datetime
import random
import time


"""
sql_cmd_stat="update attendence set status1='A'"
mycursor.execute(sql_cmd_stat)
mycursor.execute("commit")
"""

import mysql.connector
from tkinter import *
#root=Tk()
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor()
print(stud)
if(stud):
    print('successful')

def feed():
    sql_cmd="select regno from student"
    mycursor.execute(sql_cmd)
    t=mycursor.fetchall()
    f=open('class.txt','r')
    tab=f.read()
    date = datetime.date.today()
    tm = datetime.datetime.now()
    tm_hr = tm.hour
    tm = datetime.time(tm_hr, 0, 0, 0)
    for i in t:
        sql_cmd_1="insert into "+str(tab)+" values('"+str(i)+"','"+str(tm)+"','A','"+str(date)+"')"
        mycursor.execute(sql_cmd_1)
    mycursor.execute("commit")






#root=Tk()
#root.geometry('1350x750+0+0')

root=Frame(bg='white')
root.place(x=0,y=0,height=800,width=1350)



but_frm=Frame(root,bg='green',height=150,width=500)
but_frm.place(x=0,y=340)



t_now = datetime.datetime.now()
t_now1 = t_now.hour
t_min = t_now.minute
t_sec = t_now.second
t_now2 = datetime.time(t_now1,0,0,0)
t_now3=t_now.hour+1
t_now4=datetime.time(t_now3,0,0,0)
t_now5=datetime.time(t_now1,t_min,t_sec,0)



a=0
min=0
counter = 66600
running = False

t=datetime.datetime.now()
a=t.hour


tm_start=datetime.time(a,0,0,0)
tm_end=datetime.time(a+1,0,0,0)
tm1=str(tm_start)
tm2=str(tm_end)


frm=Frame(root,bg='green',height=400,width=500)
frm.place(x=840,y=330)
Label(frm,text='CLASS STARTED AT:-'+str(tm1),font="Verdana 10 bold").place(x=180,y=50)
Label(frm,text='CLASS ENDED AT:-'+str(tm2),font="Verdana 10 bold").place(x=180,y=100)
label=Label(frm, fg="black",text='YOUR TIMING:-', font="Verdana 15 bold")
label.place(x=180,y=150)
lbl1=Label(frm,text='POLL STATUS 1:-',font="Verdana 10 bold")
lbl1.place(x=50,y=300)
lbl2=Label(frm,text='POLL STATUS 2:-',font="Verdana 10 bold")
lbl2.place(x=50,y=250)
lbl3=Label(frm,text='POLL STATUS 3:-',font="Verdana 10 bold")
lbl3.place(x=250,y=250)
lbl4=Label(frm,text='POLL STATUS 4:-',font="Verdana 10 bold")
lbl4.place(x=250,y=300)
min1=0
flag=0
value=0
poll=0
def counter_label(label,flag):
    s1 = int(random.uniform(12, 17))
    s2 = int(random.uniform(28, 32))
    s3 = int(random.uniform(43, 47))
    s4 = int(random.uniform(57, 58))
    def count():
        if running:
            global counter
            global flag
            global min
            global poll

            # To manage the intial delay.
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string


            label['text'] = display
            cnt=counter-66600
            if(cnt%59==0):
                min+=1
                print(min)
                print(s1,' ',s2,' ',s3,' ',s4)
                if(min==60):
                    Stop()
                    cal(0)
                else:
                    if(min==s1):

                        if(mb.askyesno('MARK ATTENdENCE','press OK')):
                            print('present')
                            lbl1['text']='present'
                            cal(1)
                        else:
                            print('absent')
                            lbl1['text'] = 'absent'
                    if(min==s2):
                        if(mb.askyesno('MARK ATTENDENCE','press OK')):
                            print('present')
                            lbl2['text'] = 'present'
                            cal(1)
                        else:
                            print('absent')
                            lbl2['text'] = 'absent'
                    if(min==s3):
                        if(mb.askyesno('MARK ATTENDENCE','press OK')):
                            print('present')
                            lbl3['text'] = 'present'
                            cal(1)
                        else:
                            print('absent')
                            lbl3['text'] = 'absent'
                    if(min==s4):
                        if(mb.askyesno('MARK ATTENDENCE','press OK')):
                            print('present')
                            lbl4['text'] = 'present'
                            cal(1)
                        else:
                            print('absent')
                            lbl4['text'] = 'absent'

            #print(flag)
            flag=0
            #print(int(cnt/60))

            label.after(1, count)
            counter += 1

    print('poll', poll)

    # Triggering the start of the counter.

    t = datetime.datetime.now()
    b = t.hour
    if(a==b):
        count()


def Start(label):
    #print('yo')
    global running
    running = True
    counter_label(label,1)


# Stop function of the stopwatch
def Stop():
    global running
    running = False

count=0
def cal(flag_poll):
    global count

    if(flag_poll):
        count+=5
        print('a', count)
    #end_time=time.time()
    #end_time=-60*30

    t = datetime.datetime.now()
    #end_time = t.minute
    end_time = 60


    print(end_time)

    value=int(end_time-start_time)

    if(flag_poll):
        value+=5
        #print('value',value)

    global  status
    if ((value+count)>=30):
        status = 'P'
        t = datetime.datetime.now()
        a = t.hour
        f=open('regno_pswd.txt','r')
        num=f.read()
        print('******',a,'****')
        pst_time=datetime.time(a,0,0,0)
        print('pst_time',pst_time)
        dte=datetime.datetime.today()
        f = open('class.txt', 'r')
        tab = f.read()
        sql_cmd="insert into "+str(tab)+" values('"+str(num) +"','"+str(pst_time)+"','P','"+str(dte)+"')"
        #sql_cmd="update "+str(tab)+"set status1='P' where regno='"+str(num)+"' and timing='"+str(pst_time)+"' and date='"+str(dte)+"';"
        mycursor.execute(sql_cmd)
        f=open("regno_pswd.txt","r")
        reg=f.read()
        f=open("class.txt","r")
        cls=f.read()
        date=datetime.date.today()

        tm=datetime.datetime.now()
        tm_hr=tm.hour
        t=datetime.time(tm_hr,0,0,0)
        print('cls',str(cls))

        dte=datetime.date.today()



        sql_cmd_cls="update "+str(cls)+" set status1='P' where regno ='"+str(reg)+"' and timing='"+str(t)+"' and timing='"+str(dte)+"'"
        mycursor.execute(sql_cmd_cls)
        mycursor.execute("commit")
        print(str(cls))
    elif ((value+count)<50):
        status = 'A'
    Label(frm,text='total point:-'+str(value+count),bg='pink',height=2,width=65, font=('Verdana', 9)).place(x=2,y=350)

    print('status',status)

q=0
def agggregate():
    count=0
    sql_cmd_cls = "select class from Mondey_engineering"
    mycursor.execute(sql_cmd_cls)
    d_class = mycursor.fetchall()

    file=open('regno_pswd.txt','r')
    dta=file.read()

    for i in d_class:
        print(i[0])
        sql_cmd="select regno from "+str(i[0])+""
        mycursor.execute(sql_cmd)
        t=mycursor.fetchall()
        print('t',t)
        for i in t:
            print('i',i)
            if str(i[0])==str(dta):
                count+=1
                break;

    q=(count/len(d_class))*100
    print('count',count)

    sql_q = "select percentage from atd where regno='"+str(dta)+"'"
    mycursor.execute(sql_q)
    f_q = mycursor.fetchone()
    val=(q+int(f_q[0]))/2

    sql_put = "update atd set percentage='"+str(val)+"' where regno='"+str(dta)+"'"
    mycursor.execute(sql_put)
    mycursor.execute('commit')
    print('completed')


f=Frame(root).place(x=0,y=0)

t=datetime.datetime.now()
start_time=t.minute

print(start_time)
Start(label)

stop=Button(but_frm, text='LEAVE CLASS',bg='green',width=60,height=2, command=lambda :[Stop(),cal(0),agggregate()])
stop.pack()

msg=Frame(root,bg='green',height=200,width=430)
msg.place(x=0,y=500)

rule=Frame(root,bg='green',height=250,width=900)
rule.place(x=220,y=20)

file=open('rules.txt','r')
t=file.read()
Label(rule,text=t,padx=10,pady=10,bg='light green',font=('italic',13)).place(x=50,y=0)




Label(root,text='MESSAGE FACULTY',bg='green').place(x=0,y=460,width=200,height=40)
ety=Entry(msg)
ety.place(x=10,y=10,height=50,width=400)

Button(msg,text='SEND MESSAGE').place(x=50,y=100,height=50,width=300)





root.mainloop()