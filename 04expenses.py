expenses={
    'January' : 1000,
    'February': 2000,
    'March':3000,
    'April':4000,
    'May':5000,
    'June': 3000,
    'July': 4000,
    'August': 3000,
    'September': 2000,
    'October':5000,
    'November':2000,
    'December': 2300
}

total = sum(expenses.values())
length = len(expenses)

average = total/length

print(f"Total expenses of 12 months: {total}")
print(f"Average expense of 12 months: {average}")