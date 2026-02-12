# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age
age_str = input("Enter your age: ")

# Convert the age from string to integer
age = int(age_str)

# Add 1 to the age to get the age in one year
future_age = age + 1

# Print a greeting message with the user's name and future age
print(f"Hello, {name}. You will be {str(future_age)} in one year.")

# Calculate and print the number of characters in the user's name
name_length = len(name)
print(f"Your name has {name_length} characters.")