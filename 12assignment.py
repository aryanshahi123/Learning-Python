names = []

number = int(input("How many names to enter?"))

for i in range(number):
    name = input(f"Enter the name of person {i+1}:")
    names.append(name)
    print("------")
    

if len(names) != 0:
    req_names = [b for b in names if b.lower().startswith("b")]
    if len(req_names) != 0:
        print(req_names)
    else:
        print("No Names Found.")