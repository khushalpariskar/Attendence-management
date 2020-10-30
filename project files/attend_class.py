from tkinter import *
import time
#root=Tk()
#root.geometry('1350x800+0+0')
import datetime
t=datetime.date.today()
root=Frame(bg='white')
root.place(x=0,y=0,height=800,width=1350)


frm=Frame(root,bg='green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm.place(x=10,y=10)
Label(root,text='ATTENDENCE MANAGEMENT',bg='green',font=('calibri',13,'bold')).place(x=605,y=15)

main_frm=Frame(root,bg='green',height=570,width=1320,relief=GROOVE,padx=50,pady=30)
main_frm.place(x=10,y=150)



frm1=Frame(root,bg='light green',height=35,width=1320,relief=GROOVE,padx=50,pady=30)
frm1.place(x=10,y=70)
Label(root,text='ATTEND CLASS ('+str(t)+')',bg='light green',font=('calibri',13,'bold')).place(x=630,y=75)


rule_frm=Frame(root,bg='white',height=200,width=1000,relief=GROOVE,padx=50,pady=30)
rule_frm.place(x=170,y=200)

file=open('rules.txt','r')
t=file.read()
Label(rule_frm,text=t,padx=10,pady=10,bg='light green',font=('italic',13)).place(x=50,y=0)

#showing status
atd_frm=Frame(root,bg='white',height=280,width=470,relief=GROOVE,padx=50,pady=30)
atd_frm.place(x=170,y=420)
t_now = datetime.datetime.now()
t_now1 = t_now.hour
t_min = t_now.minute
t_sec = t_now.second
t_now2 = datetime.time(t_now1,0,0,0)
t_now3=t_now.hour+1
t_now4=datetime.time(t_now3,0,0,0)
t_now5=datetime.time(t_now1,t_min,t_sec,0)

def start_class():
    import atd_cal1





Label(atd_frm,text='CLASS STRATING TIME:-'+str(t_now2),padx=10,pady=10,bg='light green',font=('italic',13)).place(x=0,y=0,width=370)
Label(atd_frm,text='CLASS ENDING TIME:-'+str(t_now4),padx=10,pady=10,bg='light green',font=('italic',13)).place(x=0,y=50,width=370)
Label(atd_frm,text='you ATTENDED AT:-'+str(t_now5),padx=10,pady=10,bg='light green',font=('italic',13)).place(x=0,y=100,width=370)
Button(atd_frm,text='ATTEND CLASS:- ',padx=10,pady=10,bg='sky blue',font=('italic',13),command=start_class).place(x=0,y=175,width=180,height=30)
Button(atd_frm,text='PING FACULTY:- ',padx=10,pady=10,bg='sky blue',font=('italic',13)).place(x=200,y=175,width=180,height=30)

status_frm=Frame(root,bg='white',height=280,width=470,relief=GROOVE,padx=50,pady=30)
status_frm.place(x=700,y=420)

frm=Frame(root,bg='light green',height=30,width=470,relief=GROOVE,padx=50,pady=30)
frm.place(x=700,y=430)
Label(root,text='ATTENDENCE STATUS                         *PRESENT/ABSET*',bg='light green',font=('italic',9)).place(x=750,y=435)
Label(root,text='TOTAL TIME OF ATTENDING CLASS:-                          *counter*',font=('italic',9)).place(x=720,y=475)
Label(root,text='POLL 1 STATUS                                            *STATUS 1*',font=('italic',9)).place(x=720,y=525)
Label(root,text='POLL 1 STATUS                                            *STATUS 1*',font=('italic',9)).place(x=720,y=575)
Label(root,text='POLL 1 STATUS                                            *STATUS 1*',font=('italic',9)).place(x=720,y=625)
Label(root,text='POLL 1 STATUS                                            *STATUS 1*',font=('italic',9)).place(x=720,y=675)





root.mainloop()