# # Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your lover name? \n")

combind_name = name1.lower() + " " + name2.lower()

t = combind_name.count('t')
r = combind_name.count('r')
u = combind_name.count('u')
e = combind_name.count('e')

l = combind_name.count('l')
o = combind_name.count('o')
v = combind_name.count('v')
e = combind_name.count('e')

first_digit = t + r + u + e
second_digit = l + o + v + e

total_percentage = int(str(first_digit) + str(second_digit))

if total_percentage < 10 or total_percentage > 90:
    print(f"Your score is {total_percentage}, you go togather lile coke and mentos.")
elif total_percentage >= 40 and total_percentage <= 50:
    print(f"Your score is {total_percentage}, you are alright togather.")
else:
    print(f"Your score is {total_percentage}")