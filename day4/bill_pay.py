# Bill pay generator
import random
names = input("Give me everybodys name, separated by a comma. ")

persions = names.split(", ")

# total_persion = len(persions)
# index_to_pay = random.randrange(1, total_persion - 1)
# pay_persion = persions[index_to_pay]
pay_persion = random.choice(persions)

print(f"{pay_persion} is going to buy the meal today!")