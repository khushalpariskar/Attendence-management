from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#root=Tk()
#root.geometry('1350x750+0+0')
root=Frame(bg='white')
root.place(x=0,y=0,height=750,width=1380)
Label(root,text='ADD USER', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()


import datetime

import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor(buffered=True)
if(stud):
    print('successful')


def add(a):

    print(str(a))
    sqlFormula_student = "INSERT INTO "+str(a)+" values (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
    #sqlFormula_student_acd = "INSERT INTO student_acd values (%s, %s, %s, %s)"

    print("signing command")
    #sgn=Tk()
    #sgn.geometry("1350x700+0+0")
    #sgn.title('SIGNING ID')
    sgn=Frame(root)
    sgn.place(x=0,y=0,height=750,width=1350)
    Label(sgn, text="PERSONAL INFORMATION", bg='GREEN', width="300", height="2", font=('calibri', 13)).pack()
    Label(sgn, text="").pack()
    manage_frame = Frame(sgn, bd=4, relief=RIDGE, bg="green")
    manage_frame.place(x=170, y=100, width=1000, height=500)


#-------------------------------name-------------------
    name=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="PERSONAL NAME:-",font=('calibri',13))
    lbl.grid(row=4, column=0, pady=20, padx=20, sticky="w")
    name1=Entry(manage_frame, font=('calibri', 13),textvariable=name)
    name1.grid(row=4, column=2, padx=20, sticky="w")

#----------------------------------------------------
    gndr=StringVar()
    lbl = Label(manage_frame, text="GENDER:-", font=('calibri', 13))
    lbl.grid(row=2, column=0, pady=20, padx=20, sticky="w")
    gender=ttk.Combobox(manage_frame,font=('calibri', 13),textvariable=gndr)
    gender['values']=("male","female","other")
    gender.grid(row=2, column=2, padx=20, sticky="w")

    #-------------------------father's name-------------------
    f_name=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="FATHER'S NAME:-",font=('calibri',13))
    lbl.grid(row=6,column=0,pady=20,padx=20,sticky="w")
    f_name1=Entry(manage_frame,font=('calibri',13),textvariable=f_name)
    f_name1.grid(row=6, column=2, padx=20, sticky="w")

#------------------------mother's name--------------------
    m_name=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="MOTHER'S NAME:-",font=('calibri',13))
    lbl.grid(row=8,column=0,pady=20,padx=20,sticky="w")
    m_name1=Entry(manage_frame,font=('calibri',13),textvariable=m_name)
    m_name1.grid(row=8, column=2, padx=20, sticky="w")

#---------------------phone number------------------------
    phn_no=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="PHONE NUMBER-",font=('calibri',13))
    lbl.grid(row=2,column=10,pady=20,padx=20,sticky="w")
    phn_no1=Entry(manage_frame,font=('calibri',13),textvariable=phn_no)
    phn_no1.grid(row=2, column=11, padx=20, sticky="w")


#--------------------date of births-------------------------------
    dob=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="DATE OF BIRTH:",font=('calibri',13))
    lbl.grid(row=10,column=0,pady=20,padx=20,sticky="w")
    dob1=Entry(manage_frame,font=('calibri',13),textvariable=dob)
    dob1.grid(row=10, column=2, padx=20, sticky="w")


#-------------------email id------------------------------------------
    email=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="EMAIL ADDRESS:-",font=('calibri',13))
    lbl.grid(row=12,column=0,pady=20,padx=20,sticky="w")
    email1=Entry(manage_frame,font=('calibri',13),textvariable=email)
    email1.grid(row=12, column=2, padx=20, sticky="w")



#-----------------------------------------------------------------


#-----------------------permanent address-----------------
    pmt_add=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="PERMANENT ADDRESS:-",font=('calibri',13))
    lbl.grid(row=4,column=10,pady=20,padx=20,sticky="w")
    pmt_add1=Entry(manage_frame,font=('calibri',13),textvariable=pmt_add)
    pmt_add1.grid(row=4, column=11, padx=20,pady=10, sticky="w")

#-------------------------corresponding address-----------
    cmd_add=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="CORRESPONDING ADDRESS:-",font=('calibri',13))
    lbl.grid(row=6,column=10,padx=20,sticky="w")
    cmd_add1=Entry(manage_frame,font=('calibri',13),textvariable=cmd_add)
    cmd_add1.grid(row=6, column=11,padx=20 ,sticky="w")
    chk=Checkbutton(manage_frame,text="Same as Parmanent Address",font=('calibri',9))
    chk.grid(row=7,column=11,padx=20,sticky="w")


    regno=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="REGISTRATION NUMBER:-",font=('calibri',13))
    lbl.grid(row=8,column=10,pady=20,padx=20,sticky="w")
    regno1=Entry(manage_frame,font=('calibri',13),textvariable=regno)
    regno1.grid(row=8, column=11, padx=20,pady=10, sticky="w")


    pswd1=StringVar()
    Label(manage_frame,text="")
    lbl=Label(manage_frame,text="password-",font=('calibri',13))
    lbl.grid(row=10,column=10,pady=20,padx=20,sticky="w")
    password=Entry(manage_frame,font=('calibri',13),textvariable=pswd1)
    password.grid(row=10,column=11,pady=20,padx=20,sticky="w")


    #print(name1.get())
    #---------------------academics details--------------------------

    def acd_details():
        acd_frame = Frame(sgn, bd=4, relief=RIDGE, bg="green")
        acd_frame.place(x=170, y=100, width=1000, height=500)
      #  Label(acd_frame, text="PERSONAL INFORMATION", bg='light blue', fg='black', font=('calibri', 13)).grid(row=0,column=50,padx=0)


        regno2=StringVar()
        Label(acd_frame, text="")
        lbl = Label(acd_frame, text="PREGISTRATION NUMBER:-", font=('calibri', 13))
        lbl.grid(row=4, column=0, pady=20, padx=20, sticky="w")
        regno2=Entry(acd_frame, font=('calibri', 13),textvariable=regno2)
        regno2.grid(row=4, column=2, padx=20, sticky="w")

        sess=StringVar()
        Label(acd_frame, text="")
        lbl = Label(acd_frame, text="SELECT SESSION:-", font=('calibri', 13))
        lbl.grid(row=6, column=0, pady=20, padx=20, sticky="w")
        session = ttk.Combobox(acd_frame, font=('calibri', 13),width=10,textvariable=sess)
        session['values'] = ("2020-2021", "2019-2020", "2018-2019","2017-2018","2016-2017","2015-2016")
        session.grid(row=6, column=2, padx=20, sticky="w")


        course=StringVar()
        Label(acd_frame, text="")
        lbl = Label(acd_frame, text="SELECT COURSE:-", font=('calibri', 13),textvariable=course)
        lbl.grid(row=8, column=0, pady=20, padx=20, sticky="w")
        crse = ttk.Combobox(acd_frame, font=('calibri', 13),width=15)
        crse['values'] = (
        'Electronics and Communications Engineering (ECE)', 'Computer Science and Engineering (CSE)',
        'CSE – Internet of Things', 'Information Technology (IT)', 'Mechanical Engineering (ME)', 'Information',)
        crse.grid(row=8, column=2, padx=20, sticky="w")


        sect=StringVar()
        Label(acd_frame, text="")
        lbl = Label(acd_frame, text="ROLL NUMBER-", font=('calibri', 13))
        lbl.grid(row=10, column=0, pady=20, padx=20, sticky="w")
        section=Entry(acd_frame, font=('calibri', 13),textvariable=sect)
        section.grid(row=10, column=2, padx=20, sticky="w")
        #session.grid(row=8, column=2, padx=20, sticky="w")

        def UploadAction(event=None):
            filename = filedialog.askopenfilename()
            if(filename==1):
                Label(acd_frame,text=filename,font=('calibri', 13)).pack()
            print('Selected:', filename)

        Label(acd_frame, text="")
        lbl = Label(acd_frame, text="UPLOAD IMAGE", font=('calibri', 13))
        lbl.grid(row=4, column=50, pady=20, padx=50, sticky="w")
        Button(acd_frame,text="UPLOAD IMAGE",pady=10,padx=20,width=10,height=1,bg='sky blue',command=UploadAction).grid(row=4,column=51,sticky="w")



        Label(acd_frame, text="")
        lbl = Label(acd_frame, text="UPLOAD IDENTITY ", font=('calibri', 13))
        lbl.grid(row=5, column=50, pady=20, padx=50, sticky="w")
        Button(acd_frame,text="UPLOAD IDENTITY",pady=10,padx=20,width=10,height=1,bg='sky blue',command=UploadAction).grid(row=5,column=51,sticky="w")



        def btn11():
            print(name1.get())
            #(regno2, session, crse, section)
            student_acd1 = (regno1.get(), session.get(), crse.get(), section.get())
            mycursor.execute(sqlFormula_student_acd, student_acd1)
            stud.commit()
            messagebox.askokcancel(title='SAVED ', message='DATA SAVED SUCCESSFULLY')

        def btn22():
            if (messagebox.askyesno(title='PROCEED', message='CONFIRM?') == 1):
                main()

        Button(acd_frame, text="SAVE DATA", pady=10, padx=20, width=20, height=1, bg='sky blue', command=btn11).grid(row=10, column=50, sticky="w")
        Button(acd_frame, text="PROCEED", pady=10, padx=20, width=20, height=1, bg='crimson', command=btn22).grid(row=10, column=51, sticky="w")
    #-------------------------------------------------------------------
    def btn1():
        print(name1.get())
        student1 = (name1.get(), gender.get(), f_name1.get(), m_name1.get(), phn_no1.get(), dob1.get(), email1.get(),pmt_add1.get(), cmd_add1.get(),regno1.get(),password.get())
        mycursor.execute(sqlFormula_student, student1)
        stud.commit()

        messagebox.askokcancel(title='SAVED ', message='DATA SAVED SUCCESSFULLY')
        stud.commit()

    def btn2():
        if(messagebox.askyesno(title='PROCEED', message='CONFIRM?')==1):
            acd_details()


    Button(manage_frame,text="SAVE DATA",pady=10,padx=20,width=20,height=1,bg='sky blue',command=btn1).grid(row=13,column=10,sticky="w")
    Button(manage_frame,text="PROCEED",pady=10,padx=20,width=20,height=1,bg='crimson',command=btn2).grid(row=13,column=11,sticky="w")




lgn_frm=Frame(root)
lgn_frm.place(x=0, y=0, height=750, width=1350)
Label(lgn_frm, text='LOGIN INFORMATION', bg='GREEN', width="300", height="2", font=('calibri', 13)).pack()
Label(lgn_frm, text="").pack()
my_string=StringVar()
sel_frm=Frame(lgn_frm,bg='green')
sel_frm.place(x=355,y=90,height=300,width=650)
Label(sel_frm,text="SELECT TYPE OF USER",font=('calibri',13)).place(x=100,y=40,height=50,width=450)#combobox
user_type= ttk.Combobox(sel_frm,textvariable=my_string,font=("times new roman", 8, "bold"), state="readonly")
user_type['values'] = ("TEACHER", "STUDENT")
user_type.place(x=180,y=100,height=30,width=300)
Button(sel_frm,text="SELECT",font=("calibri", 10, "bold"),command=lambda :add(user_type.get())).place(x=180,y=180,height=40,width=300)



def main():
    lgn_frm = Frame(root)
    lgn_frm.place(x=0, y=0, height=750, width=1350)
    Label(lgn_frm, text='LOGIN INFORMATION', bg='GREEN', width="300", height="2", font=('calibri', 13)).pack()
    Label(lgn_frm, text="").pack()
    my_string = StringVar()
    sel_frm = Frame(lgn_frm, bg='green')
    sel_frm.place(x=355, y=90, height=300, width=650)
    Label(sel_frm, text="SELECT TYPE OF USER", font=('calibri', 13)).place(x=100, y=40, height=50,
                                                                           width=450)  # combobox
    user_type = ttk.Combobox(sel_frm, textvariable=my_string, font=("times new roman", 8, "bold"), state="readonly")
    user_type['values'] = ("TEACHER", "STUDENT")
    user_type.place(x=180, y=100, height=30, width=300)
    Button(sel_frm, text="SELECT", font=("calibri", 10, "bold"), command=lambda: add(user_type.get())).place(x=180,
                                                                                                             y=180,
                                                                                                             height=40,
                                                                                                             width=300)


root.mainloop()