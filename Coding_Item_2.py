import random

# Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize guess variable
guess = None

# Loop until the guess is correct
while guess != secret_number:
    # Ask for the user's guess
    guess_str = input("Guess a number between 1 and 10: ")
    guess = int(guess_str)
    
    # Check the guess
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")