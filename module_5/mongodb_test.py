from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.kfxyv48.mongodb.net/pytech";
client=MongoClient(url)
db = client.pytech
database_names=(db.list_collection_names())
print("--Pytech Collection List --")
print(database_names)
print("End of program, press any key to exit...")
input()