from product import Product

query = """
What do you want to do?
1. Add Product
2. View All Product
3. View Product With Name
4. Delete Product
(Your Query):"""
option = int(input(query))
if option == 1:
    num = int(input("Enter the number of data to enter:"))
    for i in range(num):
        p = Product(name="", qty="", price="")
        p.name = input(f"Enter product {i+1} name:")
        p.qty = input(f"Enter the quantity:")
        p.price = input(f"Enter the price:")
        p.store()
    print("Successfully Stored")
elif option == 2:
    f = open("products.csv", 'r')
    print(f.read())