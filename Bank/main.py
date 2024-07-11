from bank import Details

num = int(input("Enter the number of data to enter:"))
for i in range(num):
    p = Details(id = 0,name="", phone="", balance=0)
    p.id = int(input("Enter Id:"))
    p.name = input(f"Enter User {i+1} name:")
    p.phone= input(f"Enter the phone:")
    p.balance = float(input(f"Enter the balance:"))
    p.store()
print("Successfully Stored")
