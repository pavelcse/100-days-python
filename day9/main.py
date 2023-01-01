# # Dictionaries
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again",
# }

# # Adding New
# programming_dictionary["Another"] = "This is another dictonary."

# print(programming_dictionary)

# # define empty dictonary
# empty_dictonary = {}

# # Update the value
# programming_dictionary["Bug"] = "This bug is solved"

# print(programming_dictionary)

# # Loop in dictonary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])






# Grading Program
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     grade = ""
#     if student_scores[student] >= 80:
#         grade = "A+"
#     elif student_scores[student] >= 70:
#         grade = "A"
#     elif student_scores[student] >= 60:
#         grade = "A-"
#     elif student_scores[student] >= 50:
#         grade = "B"
#     elif student_scores[student] >= 40:
#         grade = "C"
#     elif student_scores[student] >= 33:
#         grade = "D"
#     else:
#         grade = "Fail"
        
#     student_grades[student] = grade
    

# # 🚨 Don't change the code below 👇
# print(student_grades)







# #Dictionaries, Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# # Nasting a list into dictonary
# travel_log = {
#     "France": [
#         "Paris", "Lille", "Dijon"
#         ],
#     "Germany": {
#         "Visited": ["Berlin", "Hamburg"],
#         "Total_Visited": 2
#         },
#     "Bangladesh": {
#         "Capital": "Dhaka",
#         "Currency": "Taka"
#     }
# }


# print(travel_log["Germany"][0])
# print(travel_log["Bangladesh"]["Capital"])
# print(travel_log)

# traval_log = [
#     {
#         "country": "France",
#         "visited_city": ["Paris", "Lille", "Dijon"],
#         "total_visited": 3
#     },
#     {
#         "country": "Germany",
#         "visited_city": ["Berlin", "Hamburg"],
#         "total_visited": 2
#     },
# ]