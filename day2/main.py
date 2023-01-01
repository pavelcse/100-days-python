# Data Type
#String
# print("Hello"[1])
# num_char = len(input("What is your name?\n"))
# new_str_char = str(num_char)
# print("Your name has " + new_str_char + " charecters")

# a = str(123)
# print(type(a))
#Integer
# a = 10
# b = "20"
# print(a + int(b))
#Float

#Boolean

#challenge
# number = input("Type a two digit number: ")
# first_digit = int(number[0])
# second_digit = int(number[1])
# print(first_digit + second_digit)

# Calculation
# print(3*3+3/3-3) # = 7.0
# print(3*(3+3)/3-3) # 3.0

#BMI cALCULATOR
# BMI = weight/height^2
# weight = int(input("Enter your Weight in kg: "))
# height = float(input("Enter your Height in m: "))
# bmi = weight/height**2
#print(int(bmi))

# print(8 / 3)
# print(int(8 / 3))
# print(8 // 3)
# print(round(8 / 3, 2))

# f-string
# score = 10
# height = 1.9
# isWinning = True
# print(f"Yore score is {score}, your height is {height} and you are winning is {isWinning}")

#Challange

# 1 Year = 365 days
# 1 Year = 52 weeks
# 1 Year = 12 month
age = int(input("What is your current age? "))
remaining = 90 - age
days = remaining * 365
weeks = remaining * 52
months = remaining * 12
print(f"You have {days} days, {weeks} weeks and {months} months left.")