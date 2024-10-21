#If the bill was $150.00, split between 5 people, with 12% tip. 

# bill = 150
# no = 5
# split = (150/5) * 1.12 
# print(split)

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What is the total bill? "))
persons = int(input("How many persons are there? "))
tip = int(input("What is the tip percentage? "))
factor = 1 + (tip/100)

split = (bill/persons) * factor

split = round(split, 2)

print(f"Each person should pay {split}")