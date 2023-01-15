from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.kfxyv48.mongodb.net/pytech";
client=MongoClient(url)
db = client.pytech
students=db.students
bob = {
    "student_id":"1007",
    "first_name":"Bob",
    "last_name":"Billy Bob"
}
joey={
    "student_id":"1008",
    "first_name":"Joey",
    "last_name":"Jonas"
}
kieth={
    "student_id":"1009",
    "first_name":"Keith",
    "last_name":"Koolie"
}
bob_student_id=students.insert_one(bob)
joey_student_id=students.insert_one(joey)
kieth_student_id=students.insert_one(kieth)
print("-- INSERT STATEMENTS --")
print("Inserted student record Bob Billy Bobinto the student collection with document_ID ",bob_student_id.inserted_id)
print("Inserted student record Joey Jonas into the student collection with document_ID ",joey_student_id)
print("Inserted student record Kieth Koolie into the student collection with document_ID ",kieth_student_id)
print("")
print("")
print(input("End of program, press any key to exit..."))