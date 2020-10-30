from tkinter import *
from PIL import ImageTk,Image

#from login_signing import login
#root1=Tk()
#root.geometry('1350x700+0+0')
#
import mysql.connector
import datetime

stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')


root=Frame(bg='white')
root.place(x=0,y=0,height=750,width=1350)
Label(root,text='STUDENT DASHBOARD', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()



"""
frm=Frame(root,bg='green',height=35,width=1250,relief=GROOVE)
frm.pack(padx=10,pady=10)
Label(root,text="STUDENT'S DASHBOARD",bg='white',padx=10,font=('calibri',13)).place(x=605,y=15)
"""



main_frm=Frame(root,bg='white',height=500,width=1250,relief=GROOVE)
main_frm.place(x=20,y=130)





main_frm=Frame(root,bg='white',relief=GROOVE)
main_frm.place(height=610,width=350,x=55,y=90)


main_first=Frame(root,bg='green',relief=GROOVE)
main_first.place(height=210,width=350,x=55,y=90)

pic_frm=Frame(main_first,bg='white',relief=GROOVE)
pic_frm.place(height=150,width=120,x=10,y=10)


f=open('regno_pswd.txt','r')
data=f.read()
sql_name="select name from student where regno="+data
mycursor.execute(sql_name)
data1 = mycursor.fetchone()
sql_roll="select roll from student_acd where reg_no="+data
sql_sess="select session_year from student_acd where reg_no="+data
sql_course="select course from student_acd where reg_no="+data
mycursor.execute(sql_roll)
data4 = mycursor.fetchone()
mycursor.execute(sql_sess)
data2 = mycursor.fetchone()
mycursor.execute(sql_course)
data3 = mycursor.fetchone()

Label(main_first,text='WELOCME '+str(data1[0]),padx=20,pady=20,font=('calibri',9)).place(x=150,y=40,width=150,height=60)
Label(main_first,text=data,padx=20,pady=20,font=('calibri',9)).place(x=150,y=80,width=150,height=60)





main_second=Frame(root,bg='green',relief=GROOVE)
main_second.place(height=250,width=350,x=55,y=270)



print(data1[0])



Label(main_second,text=data1,padx=20,pady=20,font=('calibri',9,'bold')).place(x=00,y=10,width=350,height=50)
Label(main_second,text=data2,padx=20,pady=20,font=('calibri',9,'bold')).place(x=00,y=80,width=350,height=50)
Label(main_second,text=data3,padx=20,pady=20,font=('calibri',9,'bold')).place(x=00,y=150,width=350,height=50)


photo=Image.open('profile.jpg')
resized=photo.resize((120,130),Image.ANTIALIAS)
profile_pic=ImageTk.PhotoImage(resized)
Label(pic_frm,image=profile_pic,width=130).pack()




tip_frm=Frame(root,bg='green',relief=GROOVE)
tip_frm.place(height=170,width=350,x=55,y=500)

f=open('quotes.txt','r')
qte=f.readline()

Label(tip_frm,text=qte,padx=20,pady=20,font=('calibri',9,'bold')).place(x=00,y=0,width=350,height=50)
Label(tip_frm,text='*QUOTE*',padx=20,pady=20,font=('calibri',9,'bold')).place(x=20,y=60,width=300,height=80)


classes=Frame(root,bg='green',relief=GROOVE)
classes.place(height=280,width=650,x=550,y=120)



def crs_atd():
    classes = Frame(root, bg='green', relief=GROOVE)
    classes.place(height=280, width=650, x=550, y=120)
    f=open('regno_pswd.txt','r')
    dta=f.read()
    sql_cmd="select percentage from atd where regno='"+str(dta)+"'"
    mycursor.execute(sql_cmd)
    t=mycursor.fetchone()

    Label(classes, text=str(t[0])+str('%'), padx=20, pady=20, font=('calibri', 13, 'bold')).place(x=250,y=60,height=100,width=100)

def tdy_cls():
    classes = Frame(root, bg='green', relief=GROOVE)
    classes.place(height=280, width=650, x=550, y=120)

    sql_cmd_date="select starting_time from Mondey_engineering"
    mycursor.execute(sql_cmd_date)
    d_time=mycursor.fetchall()
    num=len(d_time)
    sql_cmd_cls="select class from Mondey_engineering"
    mycursor.execute(sql_cmd_cls)
    d_class=mycursor.fetchall()
    print(d_class)
    for i in range(num):
        p=d_time[i][0]
        tm1=datetime.time(p, 0, 0, 0)
        tm2=datetime.time(p+1, 0, 0, 0)
        p_c=d_class[i][0]

        Label(classes,text=tm1,padx=10,pady=10, font=('calibri', 10, 'bold')).place(height=25,width=70,x=10,y=50*i)
        Label(classes,text=tm2,padx=10,pady=10, font=('calibri', 10, 'bold')).place(height=25,width=70,x=80,y=50*i)
        Label(classes,text=p_c,padx=10,pady=10, font=('calibri', 13, 'bold')).place(height=25,width=300,x=180,y=50*i)

def nws_anct():
    classes = Frame(root, bg='green', relief=GROOVE)
    classes.place(height=280, width=650, x=550, y=120)
    Label(classes, text='NEWS AND ANNOUNCEMENT WILL BE DISPLAYED HERE', padx=20, pady=20, font=('calibri', 13, 'bold')).pack()


Button(root,text="TODAY'S CLASSES",padx=50,pady=30,bg='white',font=('calibri',9,'bold'),command=tdy_cls).place(x=550,y=91,width=120,height=30)
Button(root,text="MY COURSES AND ATTENDENCE",padx=50,pady=30,bg='white',font=('calibri',9,'bold'),command=crs_atd).place(x=670,y=91,width=180,height=30)
Button(root,text="NEWS AND ANNOUNCEMENT",padx=50,pady=30,bg='white',font=('calibri',9,'bold'),command=nws_anct).place(x=850,y=91,width=252,height=30)


day_left=Frame(root,bg='green',relief=GROOVE)
day_left.place(height=220,width=280,x=550,y=420)
Label(day_left,text='NEXT HOLIDAYS',padx=50,pady=30,bg='white',font=('calibri',13,'bold')).place(x=0,y=0,width=280,height=30)
Label(day_left,text='CA',padx=50,pady=30,bg='white',font=('calibri',13,'bold')).place(x=0,y=60,width=280,height=30)
Label(day_left,text='MID-TERM',padx=50,pady=30,bg='white',font=('calibri',13,'bold')).place(x=0,y=120,width=280,height=30)
Label(day_left,text='END-TERM',padx=50,pady=30,bg='white',font=('calibri',13,'bold')).place(x=0,y=180,width=280,height=30)

my_msgs=Frame(root,bg='green',relief=GROOVE)
my_msgs.place(height=220,width=280,x=900,y=420)
Label(my_msgs,text='MY MESSAGES',padx=50,pady=30,bg='white',font=('calibri',13,'bold')).place(x=0,y=0,width=280,height=30)


#root.mainloop()
#



root.mainloop()