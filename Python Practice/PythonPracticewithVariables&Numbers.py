# -------------------------------------------
# Python - Practice with Variables & Numbers
# Karthihan Maheswaran
# 4/28/2021
# -------------------------------------------
# Question 1 - "The Name Asker 3000"
print(" ")
print("The Name Asker 3000")
name = input("Please enter your first name")
print("Hey", name, "you're going to enjoy this experience very much")

# Question 2 - Reservation for "Pick 6ix"
print(" ")
print("Welcome to the 'Pick 6ix' Reservation website")
print("Hours:" " Monday-Friday: 6:00 PM - 12:00 AM")
print("       Weekends: 7:00 PM - 3:00 AM")
print(" ")
day = input("What date are you booking to visit 'Pick 6ix'. Ex.-> DD/MM/YEAR")
time = input("What time are you booking for. Ex.-> 00:00 AM OR 00:00 PM ")
guests = input("How many guests in total for this booking")
print(" ")
print("Reservation Details")
print(day)
print('Arrive a few minutes before', time)
print(guests, "guests")
print("Can't wait to see you there!")

# Question 3 - "The Age Finder 3000"
print(" ")
print("The Age Finder 3000")
what = int(input('What year is it?'))
year = (2060 - what)
age = int(input('Please enter your age'))
years = str(age + year)
print('In the year 2060 you wil be ', years, "years old")

# Question 4 - Math Operators
print(" ")
print("Math Operators")
number_choice = int(input('Pick a number that you want to use for 4 different math operations'))
multiple = (number_choice * 4)
exponent = (number_choice ** 4)
divided = (number_choice / 4)
remainder = (number_choice - ((divided // 1) * 4))
print(number_choice, "multiplied by 4 is ", multiple)
print(number_choice, "to the exponent 4 is ", exponent)
print(number_choice, "divided by 4 is ", divided)
print("The remainder of ", number_choice, " when divided by 4 is ", remainder)

# Question 5 - Conversion of Currency
print(" ")
print("Canadian dollars to American dollars conversion")
cad = int(input("How much Canadian dollars are you trying to convert to American dollars today!"))
usd = (cad * 0.81)
print("The $", cad, "CAD your holding is equivalent to about $", usd, "USD")

# Question 6 - Loonies to Dimes & Nickels
print(" ")
print("Loonies to Dimes or Nickels")
loonies = int(input("How much loonies do you have"))
dimes = (loonies / 0.10)
nickels = (loonies / 0.05)
print("For", loonies, "loonies, it's equivalent to", dimes, "dimes", "or", nickels, "nickels")
