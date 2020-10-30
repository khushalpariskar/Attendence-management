"""
import mysql.connector
from tkinter import *
root=Tk()
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor()
print(stud)
if(stud):
    print('successful')

sqlFormula="INSERT INTO teacher values (%s, %s, %s, %s, %s, %s, %s, %s)"


name=input("ENTER NAME")
empid=int(input("ENTER EMPLOY ID"))
p_address=input("ENTER YOUR PERMANENT ADDRESS")
c_address=input("ENTER YOUR CORRESPONDING ADDRESS")
phn_no=int(input("ENTER YOUR CONTACT DETAILS"))
email=input("ENTER YOUR EMAIL ADDRESS")
dob=input("ENTER DATE OF BIRTH")
passw=input("enter password")



teacher1=(name,empid,p_address,c_address,phn_no,email,dob,passw)

mycursor.execute(sqlFormula,teacher1)
"""
"""
import mysql.connector
from tkinter import *
root=Tk()
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor()
print(stud)
if(stud):
    print('successful')



#name=input("ENTER NAME")
root=Tk()
def fun():
    name2=str(nm.get())
    print(name2)
    sqlFormula = "INSERT INTO practise values ('" + name2 + "')"
    mycursor.execute(sqlFormula)
    mycursor.execute('commit')


name=StringVar()
nm=Entry(root,textvariable=name)
nm.pack()
Button(root,command=fun).pack()


root.mainloop()

"""
#empid=int(input("ENTER EMPLOY ID"))
#p_address=input("ENTER YOUR PERMANENT ADDRESS")
#c_address=input("ENTER YOUR CORRESPONDING ADDRESS")
#phn_no=int(input("ENTER YOUR CONTACT DETAILS"))
#email=input("ENTER YOUR EMAIL ADDRESS")
#dob=input("ENTER DATE OF BIRTH")
#passw=input("enter password")
"""


#teacher1=(name,empid,p_address,c_address,phn_no,email,dob,passw)
"""

import mysql.connector
from tkinter import *
root=Tk()
stud= mysql.connector.connect(user='system', password='system',database="testdb")
mycursor=stud.cursor()
if(stud):
    print('successful')

cmd="select * from student where name='khushal' and regno='1191246'"
mycursor.execute(cmd)

data=mycursor.fetchall()

if data==[]:
    print('empty')
else:
    print('not empty')