from bank import Details
import csv

def add_customer():
    num = int(input("Enter the number of data to enter:"))
    for i in range(num):
        p = Details(id = 0,name="", phone="", balance=0)
        p.id = int(input("Enter Id:"))
        p.name = input(f"Enter User {i+1} name:")
        p.phone= input(f"Enter the phone:")
        p.balance = float(input(f"Enter the balance:"))
        p.store()

def view_all_customers():
    f = open("mainDataFile.csv", 'r')
    print(f.read())


def show_one_customer():
    reqname = input("Enter whose data you want to see?:")
    f = open("mainDataFile.csv", 'r')
    data = f.read()
    total = data.split("\n")
    for i in total:
        reqdata = i.split(",")
        if reqdata != ['']:
            if reqdata[1] == reqname:
                print(f"ID: {reqdata[0]}\nName: {reqdata[1]}\nPhone: {reqdata[2]}\nBalance: {reqdata[3]}")
    # total = csv.reader(data)
    # for row in total:
    #     if row[1] == reqname:
    #         print(f"ID: {data[0]}\nName: {data[1]}\nPhone: {data[2]}\nBalance: {data[3]}")

def view_customer_by_id():
    all_customer = []
    customer = ''

    idToFind = int(input("Enter the id:"))
    with open('mainDataFile.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            c = Details(id = int(row[0]), name = row[1], phone = row[2], balance = float(row[3]))
            all_customer.append(c)

        recordFound = False
        for c in all_customer:
            if c.id == idToFind:
                recordFound = True
                customer = c
            else:
                recordFound = False
        
        if recordFound == True:
            print("Record Is Found.")
            customer.display()
        else:
            print("Record is not found.")
            
def update_customer():
    pass

def delete_customer():
    pass