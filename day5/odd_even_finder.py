# For loop with Range
print("Sum of all Even and Odd number from 1 to 100")

# one way
sum_of_even = 0
for number in range(2, 101, 2):  # form, to, step
    sum_of_even += number
print(f"The sum of even number (Way 1): {sum_of_even}")

# another way
sum_of_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_of_even += number
print(f"The sum of even number (Way 2): {sum_of_even}")

# one way  
sum_of_odd = 0
for number in range(1, 101, 2):  # form, to, step
    sum_of_odd += number
print(f"The sum of odd number (Way 1): {sum_of_odd}")
   
# another way 
sum_of_odd = 0
for number in range(1, 101):
    if number % 2 != 0:
        sum_of_odd += number
print(f"The sum of odd number (Way 2): {sum_of_odd}")