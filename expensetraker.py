# Expense Tracker

expenses = []

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    amount = float(input(f"Enter expense {i+1}: "))
    expenses.append(amount)

total = sum(expenses)

print("\nExpense List:", expenses)
print("Total Expense:", total)