import random
print("+-+-+-+-NUMBER GUESSING GAME!-+-+-+-+")
randNumber = random.randint(0, 9)
chances = 5
print("Enter a number to guess between 0 and 9")
print(randNumber)
while chances > 0:
    userNumber = int(input("Enter your choice: "))
    if(userNumber == randNumber):
        print("Correct Choice! Congratulations!")
        chances = 0
    elif(userNumber > randNumber):
        print("Your answer is high! Try again")
        chances -= 1
        if(chances == 0):
            print("You lose!")
    else:
        print("Your answer is too low! Try again")
        chances -= 1
        if(chances == 0):
            print("You lose!")
