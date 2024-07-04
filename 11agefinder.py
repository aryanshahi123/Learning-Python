stringVal = input("Enter your string:")

def rev(value):
    length = len(value)
    str = ''
    for i in range(length ,0 , -1):
        str = str + value[i-1]
        print(str)
    

    return str

print(f"The reverse is {rev(stringVal)}")