# Initial shopping cart
cart = {'apple': 2, 'banana': 5, 'milk': 1}

# Ask to the user for item name
item = input("Enter an item to add to the cart: ").lower()  # Case-insensitive

# Check if item exists
if item in cart:
    cart[item] += 1
else:
    cart[item] = 1

# Print the cart
print("You have", end=" ")
items = list(cart.items())
for i, (item, count) in enumerate(items):
    if i == len(items) - 1:
        print(f"and {count} {item}{'s' if count > 1 else ''}.")
    else:
        print(f"{count} {item}{'s' if count > 1 else ''},", end=" ")