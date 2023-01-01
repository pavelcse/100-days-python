# print("Welcome to the rollercoaster!")
# height = int(input("what is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow tallar before you can ride!")

# Challange Odd/Even number finding
# number = int(input("What number do you want to check? "))

# if number % 2 == 0:
#     print(f"{number} is an Even Number")
# else:
#     print(f"{number} is an Odd Number")







# # BMI cALCULATOR
# # BMI = weight/height^2
# weight = int(input("Enter your Weight in kg: "))
# height = float(input("Enter your Height in m: "))
# bmi = weight/height**2
# if bmi < 18.5:
#     print(f"Your BMI is {bmi} and You are Underweight!")
# elif bmi < 25:
#     print(f"Your BMI is {bmi} and You are Nornal Weight!")
# elif bmi < 30:
#     print(f"Your BMI is {bmi} and You are Over Weight!")
# elif bmi < 35:
#     print(f"Your BMI is {bmi} and You are Obese!")
# else :
#     print(f"Your BMI is {bmi} and You are Clinically Obese!")







# # Leap Year finder
# print("Welcome to the Leap Year Finder!")
# year = int(input("What year you want to check? "))

# if year % 4 == 0:
#     if year % 100:
#         if year % 400:
#             print(f"Yes, {year} is a Leap Year")
#         else:
#             print(f"Sorry, {year} is not a Leap Year")
#     else:
#         print(f"Yes, {year} is a Leap Year")
# else:
#     print(f"Sorry, {year} is not a Leap Year")







# # Pizza Delivery
# print("Available pizza size is: S for Small, M for Medium and L for Large")
# print("Small Pizza: $15")
# print("Medium Pizza: $20")
# print("Large Pizza: $25\n")

# print("Pepperoni for Small Pizza: +$2")
# print("Pepperoni for Medium or Large Pizza: +$3\n")

# print("Extra cheese for any size pizza: +$1\n")

# size = input("What size Pizza do you want? S, M or L? ")
# add_pepperoni = input("Do you want Pepperoni? Yes or No? ")
# extra_cheese = input("Do you want extra Cheese? Yes or No? ")
# bill = 0

# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Yes":
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Yes":
#     bill += 1

# print(f"Your final bill is: ${bill}")








# # Love Calculator

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is your lover name? \n")

# combind_name = name1.lower() + " " + name2.lower()

# t = combind_name.count('t')
# r = combind_name.count('r')
# u = combind_name.count('u')
# e = combind_name.count('e')

# l = combind_name.count('l')
# o = combind_name.count('o')
# v = combind_name.count('v')
# e = combind_name.count('e')

# first_digit = t + r + u + e
# second_digit = l + o + v + e

# total_percentage = int(str(first_digit) + str(second_digit))

# if total_percentage < 10 or total_percentage > 90:
#     print(f"Your score is {total_percentage}, you go togather lile coke and mentos.")
# elif total_percentage >= 40 and total_percentage <= 50:
#     print(f"Your score is {total_percentage}, you are alright togather.")
# else:
#     print(f"Your score is {total_percentage}")






# # Treasure Finder
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the Treasure.")

left_right = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n")
if left_right == "left":
    wait_swim = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or type \"swim\" to swin across. \n")
    if wait_swim == "wait":
        read_yellow_blue = input("You arrive at the island unharmed. There is a house wuth 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which color do you choose?\n")
        if read_yellow_blue == "yellow":
            print("You found the Treasure, You win.")
        elif read_yellow_blue == "red":
            print("its a room full of fire. Game Over")
        elif read_yellow_blue == "blue":
            print("You enter a room of beasts. Game Over")
        else:
            print("You choose a door that dosnt exist. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over")


