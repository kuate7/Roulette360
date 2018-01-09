import datetime
import random


def rouletteSpin():
    rouletteSpinNumber = random.randint(0, 37)
    return rouletteSpinNumber


def oddOrEven(rouletteSpinNumber):
    if rouletteSpinNumber == 0:
        return "none"
    elif rouletteSpinNumber % 2 == 0:
        return "even"
    else:
        return "odd"


def bottomOrTopHalf(rouletteSpinNumber):
    if rouletteSpinNumber > 0 and rouletteSpinNumber <= 18:
        return "1to18"
    elif rouletteSpinNumber >= 19 and rouletteSpinNumber <= 36:
        return "19to36"


def DozenSet(rouletteSpinNumber):
    if rouletteSpinNumber > 0 and rouletteSpinNumber <= 12:
        return "1st-12"
    elif rouletteSpinNumber >= 12 and rouletteSpinNumber <= 24:
        return "2nd-12"
    elif rouletteSpinNumber >= 25 and rouletteSpinNumber <= 36:
        return "3rd-12"


def colorbet(rouletteSpinNumber):
    if rouletteSpinNumber in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25,
                              27, 30, 32, 34, 36]:
        return "red"
    elif rouletteSpinNumber in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24,
                                26, 28, 29, 31, 33, 35]:
        return "black"


# Greeting and starting balance.
print("Welcome to Roulette!")
userReadRules = input("If you want to know the payouts, please press P otherwise, any other key.")
if userReadRules == "P" or userReadRules == "p":
    print("Straight up: 35 to 1")
    print("Odd or Even: 1 to 1")
    print("Red or Black: 1 to 1")
    print("1-18 or 19-36: 1 to 1")
    print("1st, 2nd, or 3rd dozen: 2 to 1")

# Initiates user balance
userBalance = 0
userBetAmount = 301
continuePlay = "y"


while (userBalance < 1 or userBalance > 300) and userBetAmount != 0:
    userBalance = int(
        input("Please enter a starting balance not exceeding $300: ")
    )
    if userBalance > 300:
        print("Balance amount exceeds maximum starting of $300.")
    elif userBalance == 0:
        print("Starting balance cannot be 0")
    else:
        print("Your starting balance is " + str(userBalance))


while continuePlay == "Y" or continuePlay == "y" and userBalance > 0:
    print("Below are the types of bets you can play, please select one by number.")
    print("1. Straight up: Pick any number from 0,00, or 1-36")
    print("2. OddorEven: Odd or Even")
    print("3. Bottom of Top Half: 1to18 or 19-36")
    print("4. DozenSet: 1st12, 2nd12, 3rd12")
    print("5. Color: Red or Black")
#if user enters any number other than the ones listed above, the game continues.
# EX. user enters 100, game continues to display the winning value
    betType = int(input("Pick your bet: "))

    if betType == 1:
        print("A win on a single number pays 35 to 1! Good luck!!")
        # validate user amount to be is valid
        while userBetAmount > userBalance and userBalance > 0:
            userBetAmount = 0
            userBetAmount = int(input("Please enter a dollar amount to bet: "))
            if userBetAmount > userBalance:
                print("You are betting more than you have available.")
            else:
                userBalance = userBalance - userBetAmount
                print("Your new balance is " + str(userBalance))

                # Accept single number bet
                userNumber = input("Please select a number between 0 and 36, you may also select 00: ")
# user starting amt. is 100, and bets 99, system gives new balance, then prompts to select option from bet types, but reverts back to asking for dollar amt. again

    if betType == 2:
        print("Odd or even bets pay 1 to 1! Good luck!")
        while userBetAmount > userBalance and userBalance > 0:
            userBetAmount = 0
            userBetAmount = int(input("Please enter a dollar amount to bet: "))
            if userBetAmount > userBalance:
                print("You are betting more than you have available.")
            else:
                userBalance = userBalance - userBetAmount
                print("Your new balance is " + str(userBalance))

                # Accept color bet'
        userOddOrEven = input("Please select odd or even: ")

    if betType == 3:
        print("Bottom or Top Half bets pay 1 to 1! Good luck!")
        while userBetAmount > userBalance and userBalance > 0:
            userBetAmount = 0
            userBetAmount = int(input("Please enter a dollar amount to bet: "))
            if userBetAmount > userBalance:
                print("You are betting more than you have available.")
            else:
                userBalance = userBalance - userBetAmount
                print("Your new balance is " + str(userBalance))

                # Accept 1-18 or 19-36
        userBottomOrTop = input("Please select 1to18 or 19to36: ")

    if betType == 4:
        print("Dozen bets pay 2 to 1! Good luck!")
        while userBetAmount > userBalance and userBalance > 0:
            userBetAmount = 0
            userBetAmount = int(input("Please enter a dollar amount to bet: "))
            if userBetAmount > userBalance:
                print("You are betting more than you have available.")
            else:
                userBalance = userBalance - userBetAmount
                print("Your new balance is " + str(userBalance))

                # Accept 1-18 or 19-36
        userDozenSet = input("Please select 1st-12, 2nd-12, or 3rd-12: ")

    if betType == 5:
        print("Color bets pay 1 to 1! Good luck!")
        while userBetAmount > userBalance and userBalance > 0:
            userBetAmount = 0
            userBetAmount = int(input("Please enter a dollar amount to bet: "))
            if userBetAmount > userBalance:
                print("You are betting more than you have available.")
            else:
                userBalance = userBalance - userBetAmount
                print("Your new balance is " + str(userBalance))

                # Accept color bet'
        userColor = input("Please select red or black: ")

    # The below will generate a random number from 0 to 37. Number 37 will be mapped to 00
    rouletteSpinNumber = rouletteSpin()
    if rouletteSpinNumber == 37:
        rouletteSpinNumberDisplay = "00"
    else:
        rouletteSpinNumberDisplay = rouletteSpinNumber
    rouletteSpinNumberMetadata = [
        rouletteSpinNumberDisplay, oddOrEven(rouletteSpinNumber),
        bottomOrTopHalf(rouletteSpinNumber), DozenSet(rouletteSpinNumber),
        colorbet(rouletteSpinNumber)
    ]
    # reads out metadata; replaced by consolidaetd single line
    # print("The number spun is: " + str(rouletteSpinNumber))
    # print("The odd or even result is: " + oddOrEven(rouletteSpinNumber))
    # print("The 1to18 or 19to36 result is: " + bottomOrTopHalf(rouletteSpinNumber))
    # print("The dozen set result is: " + DozenSet(rouletteSpinNumber))
    # print("The color result is " + colorbet(rouletteSpinNumber))

    # save rouletteSpinNumberMetadata to a local file
    with open(datetime.datetime.now().strftime("%b_%Y_%d") +
              " Roulette History.txt", "a") as history:
        history.write(str(rouletteSpinNumberMetadata) + "\n")
        history.close()

    # Below code consolidates metadata of spun numbers
    print("The winning values are " + str(rouletteSpinNumberMetadata))

    # This code will compare the userNumber against the rouletteSpinNumber and determine win or loss message to user.
    # The input vaue from the user must first be converted to an int to be able to comare numbers, else we'll see datatype error
    # We use == to compare two values

    # if rouletteSpinNumber in rouletteSpin int(userNumber):
    #    print("You won!")
    if betType == 1:
        if userNumber in rouletteSpinNumberMetadata:
            print("You won in Straight Up single number!")
            userBalance = userBalance + int(userBetAmount) * 35
    elif betType == 2:
        if userOddOrEven in rouletteSpinNumberMetadata:
            print("You won Odd or Even bet!")
            userBalance = userBalance + int(userBetAmount) * 2
    elif betType == 3:
        if userBottomOrTop in rouletteSpinNumberMetadata:
            print("You won Bottom or Top Half!")
            userBalance = userBalance + int(userBetAmount) * 2
    elif betType == 4:
        if userDozenSet in rouletteSpinNumberMetadata:
            print("You won Dozen Set bet!")
            userBalance = userBalance + int(userBetAmount) * 3
    elif betType == 5:
        if userColor in rouletteSpinNumberMetadata:
            print("You won Color bet!")
            userBalance = userBalance + int(userBetAmount) * 2
    else:
        print("You lost! Please try again!")

    print("Your new balance is " + str(userBalance))

    if userBalance > 0:
        continuePlay = input("Enter Y if you want to continue to play.")
# Below was used for troubleshooting
        # print(continuePlay)
        # print("This is your current userBetAmount: " + str(userBetAmount))
        # print("This is your current userBalance: " + str(userBalance))
        userBetAmount = userBetAmount + userBalance
    elif userBalance == 0:
        print("You have no more funds. Thanks for playing!")
