# import random


# random_integer = random.randint(1, 10)
# print(random_integer)

# randon_float = random.random() * 5
# print(randon_float);

# # # Heads and Tails

# number = random.randint(0, 1)
# if number == 0:
#     print("Tails")
# else:
#     print("Heads")



# # List
# division = ["Khulna", "Dhaka", "Rajsahi"]
# division[2] = "Rajshahi"
# print(division[2])
# print(division[-1])

# # apend
# division.append("Barisal")

# # extend
# division.extend("Barisal")

# print(division)



# # Bill pay generator
# import random
# names = input("Give me everybodys name, separated by a comma. ")

# persions = names.split(", ")

# # total_persion = len(persions)
# # index_to_pay = random.randrange(1, total_persion - 1)
# # pay_persion = persions[index_to_pay]
# pay_persion = random.choice(persions)

# print(f"{pay_persion} is going to buy the meal today!")




# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]



#  # Tresure Map
# row1 = ["🥱", "🥱", "🥱"]
# row2 = ["🥱", "🥱", "🥱"]
# row3 = ["🥱", "🥱", "🥱"]
# print(f"{row1}\n{row2}\n{row3}")

# map = [row1, row2, row3]
# position = input("Where do you want to put the tresure? ")
# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal-1] = "😎"

# print(f"{row1}\n{row2}\n{row3}")



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