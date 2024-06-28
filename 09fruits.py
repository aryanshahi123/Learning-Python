fruits = []

num = int(input("Enter number of fruits:"))

for i in range (num):
    fruit = input(f"Enter fruit {i+1}:")
    fruits.append(fruit)

print("\n-----------------")
print("The fruits are:")
for fruit in fruits:
    print(fruit)