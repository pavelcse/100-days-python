# Student Agerage Height
print("Welcome to Height Average Counter")
# 20 30 20 35 40 20 25
student_heights = input("Input a list of student heights ").split()

# Way one using loop
total_height = 0;
total_student = 0
for height in student_heights:
    total_height += int(height)
    total_student += 1
agerage_height = round(total_height / total_student)
print(f"Student Agerage Height is {agerage_height}")

# Way 2 using default function
total_height = sum(student_heights)
total_student = len(student_heights)
agerage_height = round(total_height / total_student)
print(f"Student Agerage Height is {agerage_height}")