class Details:
    def __init__(self, id, name, phone, balance):
        self.name = name
        self.id = id
        self.phone = phone
        self.balance = balance
    
    def store(self):
        f = open("mainDataFile.csv", 'a')
        f.write(f"{self.id},{self.name},{self.phone},{self.balance}\n")
        f.close()

    def display(self):
        f = open("mainDataFile.csv", 'r')
        print(f"ID: {self.id}\nName: {self.name}\nPhone: {self.phone}\nBalance: {self.balance}")