# List of items in the store
items = ["apple", "banana", "orange", "grapes", "strawberry"]

# Prices of the items
prices = [0.99, 0.49, 0.79, 1.49, 1.99]

# Money in the user's wallet
wallet = 2.00

# Create a list of items that the user can afford
affordable_items = []

# Iterate through the items and prices
for item, price in zip(items, prices):
    # If the price is less than or equal to the money in the user's wallet,
    # add the item to the list of affordable items
    if price <= wallet:
        affordable_items.append(item)

# Sort the list of affordable items in alphabetical order
affordable_items.sort()

# Print the list of affordable items
if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
