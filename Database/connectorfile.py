import mysql.connector

def mysqlconnector():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="",
        database = "phonebook"
    )

db = mysqlconnector()
cursor = db.cursor()
name = input("Enter name:")
phone = input("Enter phone:")
cursor.execute("INSERT INTO contacts(name, phone) VALUES(%s,%s)", (name,phone))
db.commit()
db.close()
print("Success")
