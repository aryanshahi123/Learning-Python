from student import Student


is_input = True

num = int(input("How many data to enter?:"))

i = 1
while is_input and i<= num:
    name1 = input("Enter the name:")
    phone1 = input("Enter phone number:")
    st = Student(name = name1, phone = phone1 )
    st.writetofile()
    i+=1
    print("-----------------")

f = open("contacts.csv", "r")
print(f.read())