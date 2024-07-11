from bank import Details
import controller as c

query = """
What do you want to do?
1. Add User
2. View All Data
3. View User By Name
4. View User By Id
5. Update User
6. Delete User
(Your Query):"""
option = int(input(query))

if option == 1:
    c.add_customer()
    print("Successfully Stored")
elif option == 2:
    c.view_all_customers()
elif option == 3:
    c.show_one_customer()
elif option == 4:
    c.view_customer_by_id()