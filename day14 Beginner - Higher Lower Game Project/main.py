from art import logo, vs
from game_data import data
from random import choice
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def format_data(option):
    return f"{option['name']}, {option['description']}, from {option['country']}"

def check_answer(guess, option_a_follower, option_b_follower):
    if option_a_follower > option_b_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    is_continue = True
    option_b = choice(data)

    while is_continue:
        clear()
        
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")

        option_a = option_b
        option_b = choice(data)
        while option_a == option_b:
            option_b = choice(data)

        
        print(f"Compare A: {format_data(option_a)}")
        print(vs)
        print(f"Against B: {format_data(option_b)}")


        option_a_follower = option_a['follower_count']
        option_b_follower = option_b['follower_count']
        gesss = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_currect = check_answer(gesss, option_a_follower, option_b_follower)
        if(is_currect):
            score += 1
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            is_continue = False
            return
game()
