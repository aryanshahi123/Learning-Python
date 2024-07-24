import datetime

birthdate = datetime.date(2006,11,23)
currentdate = datetime.date.today()

date = datetime.datetime.now()
print(date)

diff = currentdate - birthdate
print(f"Difference is {diff}")