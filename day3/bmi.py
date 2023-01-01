# BMI cALCULATOR
# BMI = weight/height^2
weight = int(input("Enter your Weight in kg: "))
height = float(input("Enter your Height in m: "))
bmi = weight/height**2
if bmi < 18.5:
    print(f"Your BMI is {bmi} and You are Underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi} and You are Nornal Weight!")
elif bmi < 30:
    print(f"Your BMI is {bmi} and You are Over Weight!")
elif bmi < 35:
    print(f"Your BMI is {bmi} and You are Obese!")
else :
    print(f"Your BMI is {bmi} and You are Clinically Obese!")