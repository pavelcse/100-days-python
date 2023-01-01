# enemies = 1

# def increase_emenies():
#     print(f"enemies inside function: {enemies}")

# increase_emenies()
# print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)

# Global Scope
# player_helth = 20
# def drink_potion():
#     potion_strength = 2
#     print(player_helth)


# drink_potion()

# Modify global variable
enemies = 1

def increase_emenies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")
   