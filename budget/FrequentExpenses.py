from . import Expense

# Create new expenses object
expenses = Expense.Expenses()
# Read in the spending data csv
expenses.read_expenses("data/spending_data.csv")

spending_categories=[]

# Add catergories from csv to empty list
for expense in expenses.list:
    spending_categories.append(expense.category)
