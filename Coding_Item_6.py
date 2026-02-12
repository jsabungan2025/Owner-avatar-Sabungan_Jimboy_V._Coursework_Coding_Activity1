# Ask for a sentence
sentence = input("Enter a sentence: ")

# Convert to uppercase and lowercase
upper = sentence.upper()
lower = sentence.lower()
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")

# Count occurrences of "a" (case-insensitive)
count_a = sentence.lower().count('a')
print(f"The letter 'a' appears {count_a} times.")

# Check if it starts with "Hello"
starts_with_hello = sentence.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")

# Split into words and print one per line
words = sentence.split()
print("Words:")
for word in words:
    print(word)