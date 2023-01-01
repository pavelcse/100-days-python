# # Pizza Delivery
print("Available pizza size is: S for Small, M for Medium and L for Large")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25\n")

print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3\n")

print("Extra cheese for any size pizza: +$1\n")

size = input("What size Pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want Pepperoni? Yes or No? ")
extra_cheese = input("Do you want extra Cheese? Yes or No? ")
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == "Yes":
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == "Yes":
    bill += 1

print(f"Your final bill is: ${bill}")