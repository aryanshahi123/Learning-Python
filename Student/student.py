
class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def showdetails(self):
        print(f"Name: {self.name}\nPhone Number: {self.phone}")

    def writetofile(self):
        f = open("contacts.csv", 'a')
        f.write(f"Name: {self.name}\nPhone Number: {self.phone}\n------------\n")
        f.close()

