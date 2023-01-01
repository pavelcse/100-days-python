print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percerntage tip would you like to give? 10, 12 or 15? "))
people_split = int(input("How many people to split the bill? "))
amount = total_bill + (total_bill * ((percentage / 100)))
final_bill = "{:.2f}".format(round(amount / people_split, 2))
message = f"Each persion should pay: ${final_bill}"
print(message)