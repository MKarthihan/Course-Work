# -------------------------------------------
# Python - Function & Capitalization Practice Questions
# Karthihan Maheswaran
# 5/1/2021
# -------------------------------------------
# Question 1 - Volume of a sphere
def firstfunc(r):
    pie = 3.14159
    volume = 4 / 3 * pie * r ** 3
    vround = round(volume, 2)
    print("The volume of the sphere with the given parameter of 7 is", vround)
    return firstfunc


firstfunc(7)


# Question 2 - Fahrenheit to Celsius
print("")
def secfunc():
    import time
    fahrenheit = int(input("What is the Fahrenheit that you wish to convert to Celsius?"))
    celsius = ((fahrenheit - 32) * 5 / 9)
    cround = round(celsius, 2)
    print("Calculating")
    time.sleep(1)
    print("The initial,", fahrenheit, "°F", "converted to Celsius is", cround, "°C")
    return secfunc


secfunc()


# Question 3 -  3 Pieces of Information
print("")
def thirdfunc():
    import time
    Firstname = input("Enter your First name")
    Lastname = input("Enter your Last name")
    postal = input("Enter your Postal Code")
    province = input("Enter your province abbreviation")
    time.sleep(1)
    print(Firstname.title(), Lastname.title())
    print(postal.upper())
    print(province.upper())
    return thirdfunc


thirdfunc()


# Question 4 - Fibonacci code (Robertsonacci)
print("")
def Robertsonacci(x):
    r, k = 28, 29
    while r < x:
        print(r,end=" ")
        r, k = k, r+k
        print()


Robertsonacci(10000)
