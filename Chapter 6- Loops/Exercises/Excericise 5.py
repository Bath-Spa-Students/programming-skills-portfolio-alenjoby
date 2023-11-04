




# Create a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'ham and cheese', 'pastrami', 'club', 'vegetarian', 'pastrami']

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Print a message about running out of pastrami
print("Sorry, Pastrami is out of stock")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Get the first order
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
