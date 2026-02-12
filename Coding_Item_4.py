# Initial list of friends
friends = ["Jo", "Angel", "JH", "JB"]

# Print the list in the specified format
for i, friend in enumerate(friends):
    if i == 0:
        print(friend, end="")
    elif i == len(friends) - 1:
        print(f", and {friend}")
    else:
        print(f", {friend}", end="")

# Add items
friends.append("Stepen")  # Add to end
friends.insert(1, "Miguel")  # Insert at index 1

# Remove an item
friends.remove("JB")

# Sort alphabetically
friends.sort()

# Print again
print("\nSorted list:")
for i, friend in enumerate(friends):
    if i == 0:
        print(friend, end="")
    elif i == len(friends) - 1:
        print(f", and {friend}")
    else:
        print(f", {friend}", end="")