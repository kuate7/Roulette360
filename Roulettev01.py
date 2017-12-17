
import random

#setting initial starting balance for user
userBalance = 500

#The below code receives bet number and wager wager amount
print("Welcome to Roulette! Good luck! Your starting balance is $500")
print("A win on single number will multiply your bet by 37! Good luck!")
userBetAmount = input("Please enter amount to bet: ")
userNumber = input("Please select a number between 0 and 36, you may also select 00: ")


#The below will generate a random number from 0 to 37. Number 37 will be mapped to 00
rouletteSpinNumber = random.randint(0,37)
rouletteSpinNumber = 00
print("The number spun is " + str(rouletteSpinNumber))

#This code will compare the userNumber against the rouletteSpinNumber and determine win or loss message to user.
#The input vaue from the user must first be converted to an int to be able to comare numbers, else we'll see datatype error
#We use == to compare two values

if rouletteSpinNumber == int(userNumber):
    print("You won!")
    userBalance = userBalance + int(userBetAmount)*37
else:
    print("You lost! Please try again!")
    userBalance = userBalance - int(userBetAmount)

print("Your new balance is " + str(userBalance))
