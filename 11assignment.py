name = [
    # name , department
    ("santosh", "IT"),
    ("manish", "IT"),
    ("sujan", "MBA"),
    ("hari", "HR"),
    ("sari", "Micbiology"),
    ("bishwa", "software developer"),
    ("mina", "Micbiology"),
    ("rita", "HR"),
    ("sachin", "Micbiology"),
    ("gita", "HR"),

]

### Find all from Micbiology department
micbiology_name = [name for name in name if name[1] == "Micbiology"]

print(micbiology_name)

for i in micbiology_name:
    print(i[0])