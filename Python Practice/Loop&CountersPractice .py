# -------------------------------------------------------
# Loop & Counters Practice
# Karthihan Maheswaran
# 5 / 11 / 2021
# -------------------------------------------------------
# Question 1 - chr(i) function
i = 1
for i in range(256):
    print(chr(i))
    i = i + 1

print(chr(1))

# Question 2 - While function
number = int(input('Enter a amount of numbers you want added!'))
total = 0
increase = 1
while increase <= number:
    add = input('Enter number ' + str(increase) + ':')
    total = total + int(add)
    increase = increase + 1
print('The sum of all the', number, 'numbers added up is', total)

# Question 3 - For function
number = int(input('Enter a amount of numbers you want added!'))
total = 0
for increase in range(number):
    add = input('Enter number ' + str(increase + 1) + ':')
    total = total + int(add)
print('The sum of all the', number, 'numbers added up is', str(total))
