import csv
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_csv():
    try:
        with open(FILENAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount"])
    except FileExistsError:
        print("File doesn't exists!")  

def add_expense():
    date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
    if date.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")  # "string format time-makes it into a readable string" 
                                                    # datetime.now() gives the current day's date

    description = input("Enter description (e.g., Coffee at Starbucks): ")
    category = input("Enter category (e.g., Food, Travel, Rent): ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number for amount.")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])
    
    print("Expense added successfully!")

def view_expenses():
    print("\nAll Expenses:\n")
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("\t".join(str(cell) for cell in row)) # Here cell describes the variables that are inside the csv file 
    except FileNotFoundError:
        print("No expenses found. Add some first!")

def menu():
    while True:
        print("\n----- Personal Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

initialize_csv()
menu()
