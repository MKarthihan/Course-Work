# -----------------------------------
# Read and Writting to Files Practice
# Karthihan Maheswaran
# 5/17/2021
# -----------------------------------
# Opens a file that you have created
with open("datafiles/Euler.txt") as myfile:
    content = myfile.read()
    print(content)

# 4 Zoo animals
with open("datafiles/Animals.txt", "a+") as zooanimals:
    for i in range(0, 1):
        name = input("What's your name")
        animalk = input("What is your first favourite zoo animal")
        animalr = input("What is your second favourite zoo animal")
        animalf = input("What is your third favourite zoo animal")
        animall = input("What is your fourth favourite zoo animal")
        animals = (animalk, animalr, animalf, animall,)
        zooanimals.write(str(animals))
with open("datafiles/Animals.txt") as file_object:
    contents = file_object.read()
    print(name, "'s favourite four zoo animals are:", contents, )

# Series of Numbers
with open("datafiles/series.txt", "a+") as SeriesNumbers:
    for i in range(0, 1):
        number = input("Enter a number")
        numbers = input("Enter a number")
        numberss = input("Enter a number")
        numbersss = input("Enter a number")
        numberssss = number, numbers, numberss, numbersss
        SeriesNumbers.write(str(numberssss))
with open("datafiles/series.txt") as file_object:
    contents = file_object.read()
    print(contents)

# TV program
with open("datafiles/tv.txt", "a+") as TvShows:

    while True:
        tv = input("What is your favorite TV program")
        end = input("Enter 'Done'.")
        ends = end.title()
        if ends == "Done":
            break
        TvShows.write(tv)
        TvShows.write(" ")
