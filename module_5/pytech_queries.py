from collections import namedtuple
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.kfxyv48.mongodb.net/pytech";
client=MongoClient(url)
db = client.pytech
students=db.students

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for key in students.find({},{"_id":0}):
    print("Student ID: ",key["student_id"], '\n'  "First Name: ",key["first_name"], '\n'  "Last Name: ",key["last_name"], '\n' )
   
print("-- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")

one_student=students.find_one({"student_id": "1008"})
print("Student ID: ", one_student["student_id"], '\n' "First Name: ", one_student["first_name"], '\n' "Last Name: ", one_student["last_name"], '\n' '\n')
print(input("End of program, press any key to continue..."))