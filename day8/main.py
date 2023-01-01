# # Basic Function
# def great():
#     print("Hello")
#     print("How do you do")
# great()

# print("--------------------")
    
# # function with parameters
# def great_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# great_name("Pavel")\
    
# print("--------------------")
    
# # function with more then 1 parameters
# def great_with(name, location):
#     print(f"Hello {name}")
#     print(f"Welcome to {location}")
# great_with("Pavel", "Dhaka")

# print("--------------------")

# # function with positional arguments
# def great_with_positional_argument(name, deparement, designation):
#     print(f"Hello Name Is: {name}")
#     print(f"Your Deparement Is:  {deparement}")
#     print(f"Your Designation Is:  {designation}")
# great_with_positional_argument(name = "Pavel", deparement = "WEB 1", designation = "Sr, Software Engineer")





# # Paint Can calcutation
# import math
# def paint_cal(height, width, cover):
#     cans = math.ceil((height*width)/cover)
#     print(f"You'll need {cans} cans of paint")
    
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_cal(height = test_h, width = test_w, cover = coverage)





# # Prime Number checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
            
#     if is_prime:
#         print(f"{number} is a prime number because it's only divisible by 1 and {number}")
#     else:
#         print("It's not a prime number")
    
# n = int(input("Check this number: "))
# prime_checker(number = n)


# Caesar Cipher Encryption/Depcration

