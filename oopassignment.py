class Product:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def display(self):
        print(f"Product name: {self.name}\nProduct Qty: {self.qty}\nProduct Price: {self.price}")

p1 = Product(name = "Redmi Note 12", qty = 10, price = 28000)

p1.display()