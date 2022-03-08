# --------------------------------
# Module 1 –Introduction to Python
# Case Study
# --------------------------------
# Question - 1
num = int(input("Enter a number of your choice."))
print("The factors of", num, "is:")
x = 1
print(num, "multiplied by", x, ".")
print(x, "is a odd factor.")
if num % 2 == 0:
    print(num, "is a even factor.")
else:
    print(num, "is a odd factor.")

# Question - 2
sentence = input("Please enter sequences of words, with spaces between them.")
fix = sentence.title()
alpha = [word for word in fix.split(" ")]
print(" ".join(sorted(list(set(alpha)))))

# Question - 3
a = 1000
b = 3000
print("The numbers between 1000 and 3000 with all digits being even are: ")
selection = []
for i in range(a, b + 1):
    numbers = i
    isValid = True
    while numbers != 0:
        digits = numbers % 10
        numbers = numbers // 3002
        if digits % 2 != 0:
            isValid = False
            break
    if isValid:
        selection.append(i)
 print(selection)

# Question - 4
sentence = input("Enter a sequence of digits and letters of your choice.")
a = b = 0
for c in sentence:
    if c.isdigit():
        a = a + 1
    elif c.isalpha():
        b = b + 1
    else:
        pass
print("Letters:", b)
print("Digits:", a)

# Question - 5
number = input('Enter any number : ')
try:
    value = int(number)
    if number == str(number)[::-1]:
        print('The given number is Palindrome number')
    else:
        print('The given number is NOT a Palindrome number')
    except ValueError:
        print("That's not a valid number, Try Again !")
