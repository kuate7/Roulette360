
import random

#test comment for branch tracking 

def rouletteSpin():
    rouletteSpinNumber = random.randint(0,37)
    return rouletteSpinNumber


#Initiates user balance
userBalance = 0
userBetAmount = 301
continuePlay = "y"


#Greeting and starting balance.
print("Welcome to Roulette! Your maximum start balance amount is $300. Good luck!")

while (userBalance <1 or userBalance > 300) and userBetAmount != 0:
    userBalance = int(input("Please enter a starting balance not exceeding $300: "))
    if userBalance > 300:
        print("Balance amount exceeds maximum starting of $300.")
    elif userBalance == 0:
        print("Starting balance cannot be 0")
    else:
        print("Your starting balance is " + str(userBalance))

while continuePlay == "Y" or continuePlay == "y" and userBalance > 0:
    #Type of bet - only single number bets are supported at the moment.
    print("A win on a single number will multiply your bet by 37! Good luck!!")
#Below was used for troubleshooting
    #print("This is your current userBetAmount: " + str(userBetAmount))
    #print("This is your current userBalance: " + str(userBalance))
    #validate user amount to be is valid
    while userBetAmount > userBalance and userBalance > 0:
        userBetAmount = 0
        userBetAmount= int(input("Please enter a dollar amount to bet: "))
        if userBetAmount > userBalance:
            print("You are betting more than you have available.")
        else:
            userBalance = userBalance -  userBetAmount
            print("Your new balance is " + str(userBalance))

    #Start the bet 'single number'




    userNumber = input("Please select a number between 0 and 36, you may also select 00: ")


    #The below will generate a random number from 0 to 37. Number 37 will be mapped to 00
    rouletteSpinNumber = rouletteSpin()

    print("The number spun is " + str(rouletteSpinNumber))

    #This code will compare the userNumber against the rouletteSpinNumber and determine win or loss message to user.
    #The input vaue from the user must first be converted to an int to be able to comare numbers, else we'll see datatype error
    #We use == to compare two values

    if rouletteSpinNumber == int(userNumber):
        print("You won!")
        userBalance = userBalance + int(userBetAmount)*37
    else:
        print("You lost! Please try again!")

    print("Your new balance is " + str(userBalance))

    if userBalance > 0:
        continuePlay = input("Enter Y if you want to continue to play.")
#Below was used for troubleshooting
        #print(continuePlay)
        #print("This is your current userBetAmount: " + str(userBetAmount))
        #print("This is your current userBalance: " + str(userBalance))
        userBetAmount = userBetAmount + userBalance
    elif userBalance == 0:
        print("You have no more funds. Thanks for playing!")
