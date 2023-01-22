#necessary code to connect to database and collection
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.kfxyv48.mongodb.net/pytech";  # Connecting URL
client=MongoClient(url)
db = client.pytech          #Database Name
students=db.students        #collections name

#Displays using find method
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
#calls for student ID and displays all info
for key in students.find({},{"_id":0}):
    print("Student ID: ",key["student_id"], '\n'  "First Name: ",key["first_name"], '\n'  "Last Name: ",key["last_name"], '\n' )
print("")

#inserts student with the id of 1010
pippin = {
    "student_id":"1010",
    "first_name":"Pippin",
    "last_name":"Took"
}
pippin_student_id=students.insert_one(pippin)

#Displays info about student ID 1010
print("-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id ",pippin_student_id.inserted_id)
print("")
print("-- DISPLAYING STUDENT TEST DOC --")
one_student=students.find_one({"student_id": "1010"})
print("Student ID: ", one_student["student_id"], '\n' "First Name: ", one_student["first_name"], '\n' "Last Name: ", one_student["last_name"], '\n' '\n')

#deletes 1010 from database
result=students.delete_one({"student_id": "1010"})

#Displays using find method
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for key in students.find({},{"_id":0}):
    print("Student ID: ",key["student_id"], '\n'  "First Name: ",key["first_name"], '\n'  "Last Name: ",key["last_name"], '\n' )
print("")
print(input("End of program, press any key to continue..."))