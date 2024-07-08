class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name:{self.name}")
        print(f"Age: {self.age}")

st1 = Student(name = "Aryan Shahi", age = 30)
st1.display()