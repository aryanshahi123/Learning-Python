class Product:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price
    
    def store(self):
        f = open("products.csv", 'a')
        f.write(f"Product Name: {self.name}\nProduct Quantity: {self.qty}\nProduct Price: {self.price}\n----------------------\n")
        f.close()