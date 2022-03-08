# -----------------------------------------------------
# Decision Structures Practice
# Karthihan Maheswaran
# 5/6/2021
# ------------------------------------------------------
# Question 1 - Silverthorn CI. Students
import time


def cls():
    print('\n' * 100)


grade = int(input("What is your student number."))
time.sleep(1)
print("Loading...")
time.sleep(1)
cls()
name = input("What is your first name?")
last = input("What is the initial of your last name")
lasts = last.title()
time.sleep(1)
print("Loading...")
time.sleep(1)
cls()
if lasts <= "H":
    print("You must report to Mr.Brethour's office due to breaking school rules!")
elif lasts <= "Z":
    print("You must report to Ms. Hantzakos's office due to breaking school rules!")
log = input("Type 'Yes' to log out.")
if log == "Yes":
    cls()
    print("Logging off..")
    time.sleep(1)
    cls()
print("Logged off")
exit()

# Question 2 - The Mandarin Lunch time website
import time


def cls():
    print('\n' * 100)


print("Welcome to the Mandarin Lunch time website")
age = int(input("How old are you!"))
price = 16.99
print("Loading....")
time.sleep(1)
cls()
print("The Mandarin Lunch time:")
print("TODAY'S LUNCH SPECIAL")
if 5 < age < 12:
    print("The lunch price is", round((price / 2), 2), "+ tax")
elif age > 65:
    print("Then lunch price is", round((price - (price * 0.20)), 2), "+ tax")
else:
    print("The lunch price is $16.99 + tax")
print("Try our delicious honey garlic chicken wings!")
exit()

# Question 3 - Freestyle
import time


def cls():
    print('\n' * 100)


print("SCI Cross")
print("Welcome to SCI Cross's annual fundraiser to help rural areas across the globe!")
name = input("What is your name?")
mail = input("What is your email?")
ages = int(input("What is your age?"))
time.sleep(1)
if ages <= 17:
    print("Sorry, but you don't meet the required age to donate!")
    time.sleep(2)
    cls()
    exit()
else:
    print("Just wait, as we take you to the other site.")
    time.sleep(2)
    cls()
print("At SCI Cross, we give the donor the option of which Continent they would like to donate their donations.")
print("After the picked Continent from the list below, SCI Cross picks the most troubled region within the requested "
      "Continent.")
print(" ")
print("North America, South America, Europe, Africa, Asia, Antarctica")
print(" ")
continent = input("Choose a continent of which you would like donate.")
continents = continent.title()
if continents == "North America":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Your donations will be going to fund the after affect of 2020 California wildfires")
    time.sleep(8)
    cls()
elif continents == "South America":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Your donations will be going to fund St Vincent affected by La Soufrière Eruption")
    time.sleep(8)
    cls()
elif continents == "Asia":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Your donations will be going to fund citizens of Yemen with food and Family Emergency Kits")
    time.sleep(8)
    cls()
elif continents == "Africa":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Your donations will be going to fund the Water In Crisis, The Water Project in Sudan")
    time.sleep(8)
    cls()
elif continents == "Europe":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Your donations will be going to fund the movement Put the Knives away taking place in United Kingdom.")
    time.sleep(8)
    cls()
elif continents == "Antarctica":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Your donations will be going to fund the save the penguins petition throughout Antarctica.")
    time.sleep(8)
    cls()
card = int(input("Please enter your card number"))
amount = int(input("Enter the amount of CAD you would like to donate."))
time.sleep(1)
cls()
print("Loading.....")
time.sleep(1)
cls()
print("Billing:")
print(" Email:", mail)
print(" Name:", name)
print("Card #:", card)
print(" Donation Continent picked:", continents)
print(" Donation amount: $", amount, "CAD")
print(" ")
confirm = input("Type 'Yes' if you would like to confirm the donation."
                " Type 'No' if you would like to cancel the donation")
confirms = confirm.title()
if confirms == "Yes":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Donation Confirmed")
    print("Thank you!")
    exit()
elif confirms == "No":
    cls()
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    cls()
    print("Donation cancelled")
    print("ERROR")
    exit()
