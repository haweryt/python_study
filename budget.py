expenses = [
    ["кофе", 15],
    ["такси", 45],
    ["продукты", 120],
    ["кино", 35],
    ["обед", 60]
]
total_sum = 0


for i in expenses:
    total_sum += i[1]

average = total_sum / len(expenses)

print(f"Total expenses: {total_sum}")
print(f"Smallest spending {min(expenses, key=lambda x: x[1])}")
print(f"biggest spending {max(expenses, key=lambda x: x[1])}")
print(f"All spendings: {expenses}")
print(f"Average bill: {average}")