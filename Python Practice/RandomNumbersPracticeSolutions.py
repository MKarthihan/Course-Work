# Question #1 - Number picker 3000
import random

number = random.randint(1, 100)
print("The number that has been randomly chosen is: ", number)
assert number % 2 == 0
print("The number is even ")

# Question #2 - MVP Basketball player
import random

players = ["LeBron James", "Kobe Bryant", "Karthihan Maheswaran"]
mvplayer = random.choice(players)
print("The basketball player of today is", mvplayer)

# Question #3
import random

first = int(input("Enter a number of your choice: "))
second = int(input("Enter a number that's greater then your first choice number"))
print("A random number from ", first, " to ", second, " is :", random.randrange(first, second, 2))

# Question #4
import random

suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
colour = ["Red", "Black"]
card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Jack", "Queen", "King"]
random1 = random.choice(suit)
random2 = random.choice(colour)
random3 = random.choice(card)
print("Your card for the moment is a", random2, random3, "of", random1)



