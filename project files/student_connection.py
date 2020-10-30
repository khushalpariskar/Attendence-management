import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
print(stud)
if(stud):
    print('successful')

mycursor=stud.cursor()

sqlFormula="INSERT INTO student values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
name=input("ENTER NAME")
regno=int(input("ENTER REGISTRATION NUMBER"))
f_name=input("ENTER FATHER'S NAME")
m_name=input("ENTER MOTEHR'S NAME")
p_address=input("ENTER YOUR PERMANENT ADDRESS")
c_address=input("ENTER YOUR CORRESPONDING ADDRESS")
phn_no=int(input("ENTER YOUR CONTACT DETAILS"))
email=input("ENTER YOUR EMAIL ADDRESS")
dob=input("ENTER DATE OF BIRTH")
passw=input("enter password")


student1=(name, regno, f_name, m_name, p_address, c_address, phn_no, email, dob,passw)

mycursor.execute(sqlFormula,student1)

stud.commit()
