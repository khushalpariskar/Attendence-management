from tkinter import *
root=Tk()
root.title('TIME_TABLE')
root.geometry("1350x700+0+0")
Label(root,text="TODAY'S TIME TABLE", bg='sky blue',font=('calibri',20)).grid(row=0,column=18,padx=550,pady=20,sticky="n")
main_frame = Frame(root, bd=4, relief=RIDGE, bg="light grey")
main_frame.place(x=130, y=100, width=1100, height=550)


#----------------------------ongoining-class-----------------------------------
ongoing_class=Frame(main_frame, bd=4, relief=RIDGE, bg="light green")
ongoing_class.place(x=130, y=150, width=400, height=250)
Label(ongoing_class,text="ONGOINING CLASS",bg='light green',relief=RIDGE,font=('calibri',20)).grid(row=1,column=1,padx=90,pady=20)
Label(ongoing_class,text="")
Label(ongoing_class,text="class:-",font=('calibri',13)).grid(row=2,column=1,padx=0,pady=0)
Label(ongoing_class,text="")
Label(ongoing_class,text="TIMING:-",font=('calibri',13)).grid(row=4,column=1,padx=0,pady=10)
Button(ongoing_class,text="ATTEND CLASS",font=('calibri',13),width=15,height=1).grid(row=6,column=1,padx=10,pady=10,sticky="w")
Button(ongoing_class,text="APPLY LEAVE",font=('calibri',13),width=15,height=1).grid(row=6,column=1,padx=10,pady=10,sticky="e")
#-----------------------------------------------------------------------------
nxt_class=Frame(main_frame, bd=4, relief=RIDGE, bg="sky blue")
nxt_class.place(x=600, y=150, width=400, height=250)
Label(nxt_class,text="NEXT CLASS",bg='sky blue',font=('calibri',20)).grid(row=1,column=1,padx=130,pady=20)
Label(nxt_class,text="")
Label(nxt_class,text="class:-",font=('calibri',13)).grid(row=2,column=1,padx=0,pady=0)
Label(nxt_class,text="")
Label(nxt_class,text="TIMING:-",font=('calibri',13)).grid(row=4,column=1,padx=0,pady=10)
Button(nxt_class,text="APPLY LEAVE",font=('calibri',13),width=15,height=1).grid(row=6,column=1,padx=10,pady=10,sticky="w")
Button(nxt_class,text="SET REMINDER",font=('calibri',13),width=15,height=1).grid(row=6,column=1,padx=10,pady=10,sticky="e")

Button(main_frame,text="VIEW TODAY'S TIMETABLE",font=('calibri',13),width=99,height=2,bg='pink').place(x=120,y=410)

root.mainloop()
