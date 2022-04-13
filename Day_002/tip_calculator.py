
print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? > "))
number_of_people = int(input("How many people split the bill? > "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? > "))

total_amount = total_bill + ((total_bill / 100) * percentage)
amount_each = total_amount / number_of_people

print("each person should pay {0:0.1f}".format(amount_each))