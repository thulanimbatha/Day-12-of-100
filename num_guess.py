# Day project - number guess game
import random

comp_guess = random.randint(0, 100) # number between 0 and 100
user_guess = int(input("Computer has generated a random number 0-100.\nCan you guess it?\nEnter guess: "))
end_of_game = False
# number_of_guesses = 10

while user_guess != comp_guess or not end_of_game:
    if user_guess < comp_guess:
        user_guess = int(input("Too low. Try again: "))
    elif user_guess > comp_guess:
        user_guess = int(input("Too high. Try again: "))
    else:
        print(f"You guessed correctly on {user_guess}")
        end_of_game = True