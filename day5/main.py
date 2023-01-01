# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# for fruit in fruits:
#     print(fruit)





# # Student Agerage Height
# print("Welcome to Height Average Counter")
# # 20 30 20 35 40 20 25
# student_heights = input("Input a list of student heights ").split()

# # Way one using loop
# total_height = 0;
# total_student = 0
# for height in student_heights:
#     total_height += int(height)
#     total_student += 1
# agerage_height = round(total_height / total_student)
# print(f"Student Agerage Height is {agerage_height}")

# # Way 2 using default function
# total_height = sum(student_heights)
# total_student = len(student_heights)
# agerage_height = round(total_height / total_student)
# print(f"Student Agerage Height is {agerage_height}")





# # Student Height Number
# print("Welcome to Height Score Counter")
# # 71 80 87 93 88 79 90
# student_numbers = input("Input a list of student score ").split()

# # Way 1 using default function
# print(f"Student height score: {max(student_numbers)}")
# print(f"Student lowest score: {min(student_numbers)}")

# # Way 2 using loop
# height_score = 0;
# for score in student_numbers:
#     if int(score) > height_score:
#         height_score = int(score)
        
# print(f"The height score in the class is: {height_score}")



# # For loop with Range
# print("Print 1 to 100 number sum using loop with Range")

# sum_of_total = 0
# for number in range(1, 101): # form, to, step
#     sum_of_total += number
    
# print(f"The sum of total number: {sum_of_total}")



# # For loop with Range
# print("Sum of all Even and Odd number from 1 to 100")

# # one way
# sum_of_even = 0
# for number in range(2, 101, 2):  # form, to, step
#     sum_of_even += number
# print(f"The sum of even number (Way 1): {sum_of_even}")

# # another way
# sum_of_even = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         sum_of_even += number
# print(f"The sum of even number (Way 2): {sum_of_even}")

# # one way  
# sum_of_odd = 0
# for number in range(1, 101, 2):  # form, to, step
#     sum_of_odd += number
# print(f"The sum of odd number (Way 1): {sum_of_odd}")
   
# # another way 
# sum_of_odd = 0
# for number in range(1, 101):
#     if number % 2 != 0:
#         sum_of_odd += number
# print(f"The sum of odd number (Way 2): {sum_of_odd}")





# # FizzBuzz Game
# print("Welcome to FizzBuzz Game")

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)







# Password Generator
print("Welcome to Python Random Password Generator")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for password in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    
for password in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
    
for password in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

final_password = ''
for password in password_list:
    final_password += password
    
print(f"Your password is: {final_password}")