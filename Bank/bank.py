class Details:
    def __init__(self, id, name, phone, balance):
        self.name = name
        self.id = id
        self.phone = phone
        self.balance = balance
    
    def store(self):
        f = open("mainDataFile.csv", 'a')
        f.write(f"User Id: {self.id}\nUserName: {self.name}\nPhone: {self.phone}\nBalance: {self.balance}\n----------------------\n")
        f.close()