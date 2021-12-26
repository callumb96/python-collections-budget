from . import Expense
import collections
import matplotlib.pyplot as plt

# Create new expenses object
expenses = Expense.Expenses()
# Read in the spending data csv
expenses.read_expenses("data/spending_data.csv")

spending_categories=[]

# Add catergories from csv to empty list
for expense in expenses.list:
    spending_categories.append(expense.category)

# Count the categories with the most purchases
spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
# Split keys & values of top5 into separate lists
categories, count = zip(*top5)

# Initialise figure and axes
fig, ax = plt.subplots()
# Set axes as categories (x) and counts (y)
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
