names = ['Anish', 'Binod', 'Ratna', 'Suman', 'Aryan', 'Bibek']

req_names = [a for a in names if a[0].upper() == 'A']
#req_names = [a for a in names if a.startswith('A')]

print(req_names)