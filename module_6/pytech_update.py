#necessary code to connect to database and collection
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.kfxyv48.mongodb.net/pytech";  # Connecting URL
client=MongoClient(url)
db = client.pytech          #Database Name
students=db.students        #collections name

#updates the last name of 1007
result=students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

#Displays information
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
#calls for student ID and displays all info
for key in students.find({},{"_id":0}):
    print("Student ID: ",key["student_id"], '\n'  "First Name: ",key["first_name"], '\n'  "Last Name: ",key["last_name"], '\n' )

#displays updated student   
print("-- DISPLAYING STUDENT DOCUMENT FROM 1007 --")

one_student=students.find_one({"student_id": "1007"})
print("Student ID: ", one_student["student_id"], '\n' "First Name: ", one_student["first_name"], '\n' "Last Name: ", one_student["last_name"], '\n' '\n')
print(input("End of program, press any key to continue..."))