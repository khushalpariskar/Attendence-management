from tkinter import *
#from dashboard import crs_atd
#root=Tk()
#root.geometry('1350x750+0+0')
#root.title('ATTENDENCE MANAGEMENT')

root=Frame(bg='white')
root.place(x=0,y=0,height=700,width=1350)

Label(root,text='ATTENDENCE MANAGEMENT', bg='GREEN',width="300",height="2",font=('calibri',13)).pack()
Label(root,text="").pack()


def dash():
    import dashboard_adm
def std():
    import student_adm
def tch():
    import teacher_adm
def add_std_tch():
    import add_user_adm
def udp_pswd():
    import update_pswd_adm





#---------------center frame------------------
center_frame=Frame(root, bd=4, relief=RIDGE, bg="green")
center_frame.place(x=390, y=90, width=600, height=600)
#---------------------------------------------
#Button(center_frame,text="TODAY'S CLASSES",bg='orange',font=('calibri',13)),width='30',height='1').grid(row=1,column=1,padx=10,pady=10,sticky-"w") \
Label(center_frame,text="")
#Button(center_frame, text="TODAY'S CLASSES", pady=10, padx=20, width=60, height=1, bg='sky blue').grid(row=2, column=1)
Button(center_frame, text="DASHBOARD", bg='sky blue',command=lambda:dash()).place(x=130,y=40,width=320,height=45)
Button(center_frame, text="STUDENTS", bg='sky blue',command=lambda:std()).place(x=130,y=95,width=320,height=45)
Button(center_frame, text="TEACHERS", bg='sky blue',command=lambda:tch()).place(x=130,y=148,width=320,height=45)
Button(center_frame, text="ADD USER", bg='sky blue',command=lambda:add_std_tch()).place(x=130,y=203,width=320,height=45)
Button(center_frame, text="UPDATE PASSWORD", bg='sky blue',command=lambda:udp_pswd()).place(x=130,y=258,width=320,height=45)
Button(center_frame, text="LOGOUT", bg='sky blue',).place(x=130,y=313,width=320,height=45)


root.mainloop()