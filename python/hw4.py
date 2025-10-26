# Number Guessing Game. The program chooses a secret random number between 1
# and 100. The user has a limited number of attempts (5) to guess it.
# After each guess, the program tells the user if their guess was
# "too high," "too low," or "correct."

import random

secret_number = random.randint(1, 100)
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if attempts == 5:
    print("You lost! The number was", secret_number)
