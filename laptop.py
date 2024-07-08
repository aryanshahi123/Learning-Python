class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name
        self.ram = ram
    
    def display(self):
        print(f"ID: {self.id}\nName: {self.name}\nRAM: {self.ram}GB")
        print("---------------------")


l1 = Laptop(id = 1, name = "Dell G3 1590", ram = 8)
l2 = Laptop(id = 2, name = "Acer Nitro 5", ram = 16)
l3 = Laptop(id = 3, name = "HP Victus 15", ram = 16)

l1.display()
l2.display()
l3.display()