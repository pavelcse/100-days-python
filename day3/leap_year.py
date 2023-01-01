# Leap Year finder
print("Welcome to the Leap Year Finder!")
year = int(input("What year you want to check? "))

if year % 4 == 0:
    if year % 100:
        if year % 400:
            print(f"Yes, {year} is a Leap Year")
        else:
            print(f"Sorry, {year} is not a Leap Year")
    else:
        print(f"Yes, {year} is a Leap Year")
else:
    print(f"Sorry, {year} is not a Leap Year")