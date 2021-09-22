# Day project - number guess game
from random import randint

EASY_LEVEL_NUM = 10
HARD_LEVEL_NUM = 5

# 4 - check user guess
def check_answer(user_guess, comp_guess, tries):
    if user_guess > comp_guess:
        print("Too high.")
        return tries - 1
    elif user_guess < comp_guess:
        print("Too low")
        return tries - 1
    else:
        print(f"You win. The computer chose {comp_guess}")

# 2 - set difficulty
def set_difficulty():
    level = input("Choose a difficulty. (type 'easy' or 'hard'): ").lower()
    if level == "easy":
        return EASY_LEVEL_NUM
    else:
        return HARD_LEVEL_NUM

'''PROGRAM START'''
def num_guess():
    # 1 - comp choose random number between 1 - 100
    print("Welcome to the Guessing Game! Can you beat the computer?")
    comp_guess = randint(1, 100)
    print("Computer chose a number between 1 and 100. See if you can guess it.")

    # 3 - let user guess number
    number_of_guesses = set_difficulty()

    user_guess = -1

    # 6 - repeat if user gets guess wrong
    while user_guess != comp_guess :
        print(f"You have {number_of_guesses} attempts left.")

        user_guess = int(input("Make your guess: "))

        # 5 - track number of guesses
        number_of_guesses = check_answer(user_guess, comp_guess, number_of_guesses)

        if number_of_guesses == 0:
            print("You have run out of guesses! Goodbye!")
            return

num_guess()