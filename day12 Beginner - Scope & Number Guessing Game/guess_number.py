#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint
from os import system, name

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def choode_difficulty():
    type = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if type == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    clear()
    print(logo)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 amd 100.")

    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    
    turns = choode_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")

game()