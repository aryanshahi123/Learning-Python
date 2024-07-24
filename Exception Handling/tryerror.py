try:
    birthyear = input("Enter birthyear")
    age = 2024 - int(birthyear)
    print(f"Your age is {age}")
except:
    print("Valid date in numeric values")
finally:
    print("Program Closing")