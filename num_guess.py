# Day project - number guess game
import random

comp_guess = random.randint(0, 100) # number between 0 and 100
user_guess = int(input("Computer has generated a random number 0-100.\nCan you guess it?\nEnter guess: "))

if user_guess < comp_guess:
    print("Too low")
elif user_guess > comp_guess:
    print("Too high")
else:
    print(f"You guessed correctly on {user_guess}")