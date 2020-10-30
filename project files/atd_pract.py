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


root=Tk()
root.geometry('1350x750+0+0')

root=Frame(bg='white')
root.place(x=0,y=0,height=700,width=1350)

def atd():
    a = 0
    min = 0
    counter = 66600
    running = False

    t = datetime.datetime.now()
    a = t.hour

    tm_start = datetime.time(a, 0, 0, 0)
    tm_end = datetime.time(a + 1, 0, 0, 0)
    tm1 = str(tm_start)
    tm2 = str(tm_end)

    frm = Frame(root, bg='green', height=400, width=500)
    frm.place(x=500, y=50)
    Label(root, text='CLASS STARTED AT:-' + str(tm1)).place(x=600, y=80)
    Label(root, text='CLASS ENDED AT:-' + str(tm2)).place(x=600, y=120)
    label = Label(root, fg="black", text='YOUR TIMING:-', font="Verdana 15 bold")
    label.place(x=600, y=160)
    lbl1 = Label(root, text='POLL STATUS 1:-')
    lbl1.place(x=600, y=220)
    lbl2 = Label(root, text='POLL STATUS 2:-')
    lbl2.place(x=600, y=260)
    lbl3 = Label(root, text='POLL STATUS 3:-')
    lbl3.place(x=600, y=300)
    lbl4 = Label(root, text='POLL STATUS 4:-')
    lbl4.place(x=600, y=340)
    min1 = 0
    flag = 0
    value = 0
    poll = 0

    def counter_label(label, flag):
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
                cnt = counter - 66600
                if (cnt % 59 == 0):
                    min += 1
                    print(min)
                    print(s1, ' ', s2, ' ', s3, ' ', s4)
                    if (min == 60):
                        Stop()
                        cal(0)
                    else:
                        if (min == s1):

                            if (mb.askyesno('MARK ATTENdENCE', 'press OK')):
                                print('present')
                                lbl1['text'] = 'present'
                                cal(1)
                            else:
                                print('absent')
                                lbl1['text'] = 'absent'
                        if (min == s2):
                            if (mb.askyesno('MARK ATTENDENCE', 'press OK')):
                                print('present')
                                lbl2['text'] = 'present'
                                cal(1)
                            else:
                                print('absent')
                                lbl2['text'] = 'absent'
                        if (min == s3):
                            if (mb.askyesno('MARK ATTENDENCE', 'press OK')):
                                print('present')
                                lbl3['text'] = 'present'
                                cal(1)
                            else:
                                print('absent')
                                lbl3['text'] = 'absent'
                        if (min == s4):
                            if (mb.askyesno('MARK ATTENDENCE', 'press OK')):
                                print('present')
                                lbl4['text'] = 'present'
                                cal(1)
                            else:
                                print('absent')
                                lbl4['text'] = 'absent'

                # print(flag)
                flag = 0
                # print(int(cnt/60))

                label.after(10, count)
                counter += 1

        print('poll', poll)

        # Triggering the start of the counter.

        t = datetime.datetime.now()
        b = t.hour
        if (a == b):
            count()

    def Start(label):
        # print('yo')
        global running
        running = True
        counter_label(label, 1)

    # Stop function of the stopwatch
    def Stop():
        global running
        running = False

    count = 0

    def cal(flag_poll):
        global count

        if (flag_poll):
            count += 5
            print('a', count)
        # end_time=time.time()
        # end_time=-60*30

        t = datetime.datetime.now()
        # end_time = t.minute
        end_time = 60

        print(end_time)

        value = int(end_time - start_time)

        if (flag_poll):
            value += 5
            # print('value',value)

        global status
        if ((value + count) >= 20):
            status = 'P'
            t = datetime.datetime.now()
            a = t.hour
            f = open('regno_pswd.txt', 'r')
            num = f.read()
            print('******', a, '****')
            pst_time = datetime.time(a, 0, 0, 0)
            print('pst_time', pst_time)
            sql_cmd = "insert into attendence values('" + num + "','P','" + str(pst_time) + "')"
            mycursor.execute(sql_cmd)
            f = open("regno_pswd.txt", "r")
            reg = f.read()
            f = open("class.txt", "r")
            cls = f.read()
            date = datetime.date.today()

            sql_cmd_cls = "update " + str(cls) + " set status1='P' where regno ='" + str(reg) + "'"
            mycursor.execute(sql_cmd_cls)
            mycursor.execute("commit")

        elif ((value + count) < 50):
            status = 'A'
        Label(frm, text='total point:-' + str(value + count), bg='pink', height=2, width=65, font=('Verdana', 9)).place(
            x=2, y=350)

        print('status', status)

    0

    f = Frame(root).place(x=0, y=0)

    t = datetime.datetime.now()
    start_time = t.minute

    print(start_time)
    Start(label)

    stop = Button(f, text='LEAVE CLASS', bg='green', width=60, height=2, command=lambda: [Stop(), cal(0)])
    stop.place(x=10, y=150)



atd()
root.mainloop()