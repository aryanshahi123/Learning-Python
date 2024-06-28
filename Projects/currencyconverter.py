npr = float(input("Enter money in Nepali Rupees:"))

usd = npr/133
euro = npr/143
yen = npr * 1.19

print(f"The value of Rs.{npr} is \n")
print(f"${usd}\t£{euro}\t¥{yen}")