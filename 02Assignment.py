#Store your expenses from sunday to saturday and find total expenses and total expenses

sunday_exp = 1200
monday_exp = 500
tuesday_exp = 1500
wednesday_exp = 2500
thursday_exp = 1700
friday_exp = 1050
saturday_exp = 3000

total_exp = sunday_exp + monday_exp + tuesday_exp + wednesday_exp + thursday_exp + friday_exp + saturday_exp
average_exp = total_exp/7

print(f"Total Expenses = Rs{total_exp}")
print(f"Average Expense = Rs{average_exp}")