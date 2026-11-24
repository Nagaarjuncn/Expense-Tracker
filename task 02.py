import csv
from datetime import datetime

file_name = "expenses.csv"
headers = ["date", "category", "amount"]

try:
    open(file_name, "r").close()
except FileNotFoundError:
    with open(file_name, "w", newline="") as f:
        csv.DictWriter(f, fieldnames=headers).writeheader()

while True:
    choice = input("\n1. Add Expense  2. View Totals  3. Exit: ")

    if choice == "1":
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ").strip().title()
        amount = input("Amount: ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
        except ValueError:
            print("Invalid date or amount! Try again.")
            continue

        row = {"date": date, "category": category, "amount": amount}
        with open(file_name, "a", newline="") as f:
            csv.DictWriter(f, fieldnames=headers).writerow(row)
        print("Saved!")

    elif choice == "2":
        totals = {}
        with open(file_name, "r") as f:
            for row in csv.DictReader(f):
                cat = row["category"]
                totals[cat] = totals.get(cat, 0) + float(row["amount"])

        for cat, total in totals.items():
            print(f"{cat}: {total}")

    elif choice == "3":
        break
