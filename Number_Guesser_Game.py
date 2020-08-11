# Imports go here
import random


# The Random number lol and defining "random_1"
def random_1():
    RNG = random.randrange(1, 10, 1)

    #Hint Section
    if RNG == 1:
        print("Answer * X = X")
        return 1
    if RNG == 2:
        print("Answer * X = even number")
        return 2
    if RNG == 3:
        print("The Answer is 3")
        return 3
    if RNG == 4:
        print("4")
        return 4
    if RNG == 5:
        print("Answer^X = ends with 5")
        return 5
    if RNG == 6:
        print("6")
        return 6
    if RNG == 7:
        print("7")
        return 7
    if RNG == 8:
        print("8")
        return 8
    if RNG == 9:
        print("9")
        return 9
    if RNG == 10:
        print("10")
        return 10


#Welcoming the User
print(
    "Welcome to the Number Guesser Game! Please note that the answer is between 1 and 10 "
)
#Answering the input
n = 0
loop = True
while loop:
    if n == 10:
        print("YOU WON THE GAME!!")
        break
    a = random_1()
    while loop:
        try:
            answer = int(input("Answer: "))
            if answer == a:
                print("You got it")
                n += 1
                break
            else:
                print("Incorrect, Please try again")
                continue
        except ValueError:
            print("Please enter a Valid Number")
