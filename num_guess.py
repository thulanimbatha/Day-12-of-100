# Day project - number guess game
import random

def num_guess():
    comp_guess = random.randint(0, 100) # number between 0 and 100
    user_guess = int(input("Computer has generated a random number 0-100.\nCan you guess it?\nEnter guess: "))
    end_of_game = False
    number_of_guesses = 4

    while not end_of_game and number_of_guesses >= 0:
        print(f"\tYou have {number_of_guesses} guesses left.")
        if user_guess < comp_guess:
            number_of_guesses -= 1
            user_guess = int(input("Too low. Try again: "))
        elif user_guess > comp_guess:
            number_of_guesses -= 1
            user_guess = int(input("Too high. Try again: ")) 
        elif user_guess == comp_guess:
            print(f"You guessed correctly on {user_guess}")
            end_of_game = True
 
num_guess()