import random

#Greeting Message
print("Welcome to the game of Rock-Paper-Scissors")

#Initialization
gamesPerTournament = 3
userWins = 0
cpuWins = 0
terminate = False
game = 0
roundNum = 0
cpuString = " "
cpuChoice = 0

#Start Game
while not terminate:
    roundNum = roundNum + 1
    game = game + 1

    #Prints the round number
    print("\nGame " + str(roundNum) + ":")

    #Get userChoice from user
    userChoice = int(input("Make a choice: 1-Rock, 2-Paper, 3-Scissors: "))

    #Get cpuChoice and convert random int from 1-100
    #to a number 1-3 and a string value
    cpuChoice = random.randint(1, 100)
    if cpuChoice != None:
        if cpuChoice <= 33:
            cpuChoice = 1
            cpuString = "1-Rock"
        if 33 < cpuChoice <= 66:
             cpuChoice = 2
             cpuString = "2-Paper"
        if cpuChoice > 66:
            cpuChoice = 3
            cpuString = "3-Scissors"

    #Check if userChoice is equal to cpuChoice
    if userChoice == cpuChoice:
        print("\nThe computer choice is: " + cpuString)
        print("\nThe game is a draw")
        print("\nScore: User: " + str(userWins) + " - Computer: " +str(cpuWins))
        game = game - 1

    #Check if userChoice equals to 1 against cpuChoice
    elif userChoice == 1:
        print("\nThe computer choice is: " + cpuString)
        if cpuChoice == 2:
            print("\nYou lose")
            cpuWins = cpuWins + 1
            print("\nScore: User: " + str(userWins) + " - Computer: " + str(cpuWins))
        else:
            print("\nYou win!")
            userWins = userWins + 1
            print("\nScore: User: " + str(userWins) + " - Computer: " + str(cpuWins))

    #Check if userChoice is equal to 2 against cpuChoice
    elif userChoice == 2:
        print("\nThe computer choice is: " + cpuString)
        if cpuChoice == 1:
            print("\nYou win")
            userWins = userWins + 1
            print("\nScore: User: " + str(userWins) + " - Computer: " + str(cpuWins))
        else:
            print("\nYou lose")
            cpuWins = cpuWins + 1
            print("\nScore: User: " + str(userWins) + " - Computer: " + str(cpuWins))

    #Check if userChoice is equal to 3 against cpuChoice
    elif userChoice == 3:
        print("\nThe computer choice is: " + cpuString)
        if cpuChoice == 1:
            print("\nYou lose")
            cpuWins = cpuWins + 1
            print("\nScore: User: " + str(userWins) + " - Computer: " + str(cpuWins))
        else:
            print("\nYou win")
            userWins = userWins + 1
            print("\nScore: User: " + str(userWins) + " - Computer: " + str(cpuWins))

    ##If userWins equal 2 end game and give option to start again
    if userWins == 2:
        print("\nUSER is the WINNER!!!")
        playAgain = input("\nDo you want to play another tournament? (y/n) ")
        if playAgain == "y":
            game = 0
            roundNum = 0
            userWins = 0
            cpuWins = 0
        elif playAgain == "n":
            print("Have a great day!")
            terminate = True

    ##If cpuWins equal 2 end game and give option to start again
    if cpuWins == 2:
        print("CPU is the WINNER!!!")
        playAgain = input("Do you want to play another tournament? (y/n) ")
        if playAgain == "y":
            game = 0
            roundNum = 0
            userWins = 0
            cpuWins = 0
        elif playAgain == "n":
            print("Have a great day!")
            terminate = True