# Expense Tracker

A simple command-line Python application to record daily expenses, validate inputs, store records in a CSV file, and calculate total spending by category.

## Features
- **CSV Storage with Dictionaries:** Uses Python's `csv.DictWriter` and `csv.DictReader` to store and read expense records as structured dictionaries (`date`, `category`, `amount`).
- **Input Validation:** Verifies that dates follow the `YYYY-MM-DD` format and ensures amounts are valid positive numbers before saving.
- **Category Totals:** Automatically groups and sums spending across categories.
- **Spreadsheet Compatible:** Outputs a standard `expenses.csv` file that can be opened directly in Microsoft Excel, Google Sheets, or LibreOffice Calc.

## Requirements
- Python 3.x (uses only built-in `csv` and `datetime` modules—no external installations required)

## How to Run
1. Open a terminal or command prompt in the project directory.
2. Run the script:
   ```bash
   python "task 02.py"