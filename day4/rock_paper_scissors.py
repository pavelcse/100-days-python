# # Rock, Paper, Scissors
# # Rock > Scissors > Paper > Rock

# # Rock > Scissors
# # Scissors > Paper
# # Paper > Rock

import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if user >= 3 or user < 0:
    print("Please type the correct number! You Lose!") 
else:
    game_images = [rock, paper, scissors]
    game_term = ["Rock", "Paper", "Scissors"]

    print(game_images[user])
    print(f"You choose {game_term[user]}")

    print(game_images[computer])
    print(f"Computer choose {game_term[computer]}")
    
    if user == 0 and computer == 2:
        print("You Win!")
    elif computer == 0 and user == 2:
        print("You Lose!")
    elif user < computer:
        print("You Lose!")
    elif user > computer:
        print("You Win!")
    elif user == computer:
        print("Its a Draw!")