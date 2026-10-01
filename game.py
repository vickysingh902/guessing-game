import random

secret_number = random.randint(1, 10)

print("Welcome to Number Guessing Game!")

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You won!")
        break