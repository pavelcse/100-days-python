# Student Height Number
print("Welcome to Height Score Counter")
# 71 80 87 93 88 79 90
student_numbers = input("Input a list of student score ").split()

# Way 1 using default function
print(f"Student height score: {max(student_numbers)}")
print(f"Student lowest score: {min(student_numbers)}")

# Way 2 using loop
height_score = 0;
for score in student_numbers:
    if int(score) > height_score:
        height_score = int(score)
        
print(f"The height score in the class is: {height_score}")