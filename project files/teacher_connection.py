import mysql.connector
stud= mysql.connector.connect(user='system', password='system',database="testdb")
print(stud)
if(stud):
    print('successful')

mycursor=stud.cursor()

sqlFormula="INSERT INTO teacher values (%s, %s, %s, %s, %s, %s, %s, %s)"


name=input("ENTER NAME")
empid=int(input("ENTER EMPLOY ID"))
p_address=input("ENTER YOUR PERMANENT ADDRESS")
c_address=input("ENTER YOUR CORRESPONDING ADDRESS")
phn_no=int(input("ENTER YOUR CONTACT DETAILS"))
email=input("ENTER YOUR EMAIL ADDRESS")
dob=input("ENTER DATE OF BIRTH")
passw=input("enter password")



empid=int(input("ENTER EMPLOY ID"))
courses=input("ENTER COURSES")
sqlFormula1="INSERT INTO teacher_acd values (%s, %s)"

teacher1=(name,empid,p_address,c_address,phn_no,email,dob,passw)
teacher2=(empid,courses)

mycursor.execute(sqlFormula,teacher1)
mycursor.execute(sqlFormula1,teacher2)