details = [
    ("Aryan Shahi", "Software Developer"),
    ("Rajat Somani", "IT Department"),
    ("Rachin Giri", "Finance"),
    ("Bhuwan KC", "Actor"),
    ("Suman Karki", "IT Department"),
    ("Sujan Bishwokarma", "Cleaner"),
    ("Rajan Thapa", "Helper"),
    ("Lucky Kumar", "Teacher"),
    ("Santosh Jha", "IT Department"),
    ("Rajaram Pander", "Singer")
]

it_details = [x for x in details if x[1]=="IT Department"]

for i in it_details:
    print(f"Name:{i[0]}\nDepartment:{i[1]}")
    print("------------------")