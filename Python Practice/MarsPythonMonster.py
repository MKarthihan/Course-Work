# -------------------------------------
# Mars Python Monster
# Creators: Bilal Rashid & Karthihan Maheswaran
# 5/4/2021
# -------------------------------------
# Importing Python modules
import time
import math
import random


def slope_formula():
    y_2 = int(input("Please enter the value for y₂ : "))
    print("\n")
    y_1 = int(input("Please enter the value for y₁ : "))
    print("\n")
    x_2 = int(input("Please enter the value for x₂ : "))
    print("\n")
    x_1 = int(input("Please enter the value for x₁ : "))
    print("\n")
    return (y_2 - y_1) / (x_2 - x_1)


# Function for generating a random number
def random_number():
    a = random.randint(1, 100)
    return a


# Function for generating a random city you'll be going to
def list_of_cites():
    random_cities_dic = ['Toronto, Canada', "Tehran, Iran", 'Warsaw, Poland', 'Bordeaux, France',
                         'Amsterdam, Netherlands']
    random_cities = random.choice(random_cities_dic)
    return random_cities


# Function for determining whether a number is odd or even
def odd_or_even():
    odd_or_even_ = int(input("Please enter a number that you wanna if it is odd or even: "))
    if odd_or_even_ % 2 == 0:
        print("The number", odd_or_even_, "is even!")
    else:
        print("The number", odd_or_even_, "is odd!")


# Function for probability
def probability():
    input_1 = input(
        "Please enter a question of your choice and the One-eyed monster will tell you the probability of it "
        "happening: ")
    a_list_1 = ["a 100% chance", "a 75% chance", "a 50% chance", "a 25% chance", "a 0% chance"]
    random_1 = random.choice(a_list_1)
    print("The probability of", input_1, "is", random_1, "!")


# Main function helps run the program
def cls():
    print('\n' * 100)


print("Welcome to Mars human! I am the Monster of Mars, they call me 'One eye'.")
print("\n")
name = input("What's your name? ")
print("\n")
print("Cool name,", name, "never heard that one before here!")
time.sleep(5)
cls()

print("I have a few questions to ask you, before we get into the 'Lair of Exclusive Questions' that I have for worthy "
      "humans that come to Mars.")
print("\n")
time.sleep(7)
cls()

height = int(input("How tall are you? Enter your height in 'CM': "))
print("\n")
time.sleep(1)
print("Interesting...", height, "CM")
print("\n")
time.sleep(1)
print("Next question")
print("\n")
time.sleep(3)
cls()

answer = int(input("If there 2 humans on Mars, and I eat 1, how many humans are left on Mars?"))
print("\n")
if not answer == 1:
    print("Come on now! Sorry, but I have to do this")
    time.sleep(2)
    print("YOU HAVE BEEN EATEN BY THE MONSTER!")
    exit()
if answer == 1:
    print("HAHA, you're very smart!")
    time.sleep(3)
    cls()
print("\n")

print("This is the final question before getting into the 'Lair of Exclusive Questions'!")
print("\n")
eye = "One eye"
eyename = input("What is my name? HINT: 👁️ ")
print("\n")
if not eyename == eye:
    print("You're not worthy!")
    print("\n")
    time.sleep(2)
    print("YOU HAVE BEEN EATEN BY THE MONSTER!")
    print("\n")
    exit()
if eyename == eye:
    print("You have my respect", name, ", I am always under your command from now on")
    time.sleep(3)
    cls()

print("Congratulations, you have entered the 'Lair of Exclusive Questions'!")
print("\n")
input_1 = int(input("Please enter the number '0' to have a look at the five questions! "))
print("\n")
questions = [
    "Q-1 : Wanna calculate the slope between two points, use the slope formula funciton, press 1 to use the function! "
    "This function may raise an error because you are diving by zero if you enter certain values, for example, "
    "if you say y₂= 1, y₁= 1, x₂= 1, and x₁ = 0 too, the function will raise an error because (1-1)/(1-1) = 0/0 = "
    "MathError. This raises an error because anything in math divide by 0 gives an error.",
    "Q-2: Wanna generate a random number, press 2 two use the funciton!",
    "Q-3: Wanna visits a random country next month, enter number 3 to get to know where you are headed!",
    "Q-4: Enter a random number and the function will tell you whether it is odd or even, press number 4 to go to "
    "this function!",
    "Q-5: Wanna know the probability of something enter number 5 to go the function!"]

if input_1 == 0:
    print(*questions, sep="\n")
else:
    print("You didn't want any questions to be printed so the program ended!")

questions_number_selected = int(input("Please enter the number corresponding to what question you want answered: "))
print("\n")
if questions_number_selected == 1:
    print("\n")
    print("The slope is", slope_formula(), "!")
elif questions_number_selected == 2:
    print("\n")
    print("The random number is", random_number(), "!")
elif questions_number_selected == 3:
    print("\n")
    print("Woo hoo, you're ticket it booked packs your bags. Next month you are visiting", list_of_cites(), "!")
elif questions_number_selected == 4:
    print("\n")
    print(odd_or_even())
elif questions_number_selected == 5:
    print(probability())

print("\n")
number = input('If you wanna exit the program and you wanna know a bit more about the One-eyed monster press 0! ')
if int(number) == 0:
    cls()
print("Hey there,", name,
      ". Before you leave to earth, we would like to let you know more about the One eye monster. The One eye "
      "monster is a unique breed of the lost Oompa Loompas. They are very caring to their masters, but also very "
      "dangerous to unknown humans. One eye will miss you after you leave Mars.")
time.sleep(20)
