Roulette 360 App

The purpose of this repo is to enable best practice code collaboration for the gptx360devteam.

The code itself will mirror the casino game Roulette.

Roulettev01.py was the initial set of code to help get the game started.  Code had no clean structure other than forcing code to come together.  While not complete, it helped set the stage and learn how python could be used to get user entry and bounce it against the basic rules of the game.

Roulettev02-refactored.py is the next iteration for this project.   Here the code is broken down into smaller functions that serve a purpose.  To start out, the roulettespin() function gets us a simulated random spin which is then passed to the secondary functions to read what that number translates to i.e. Red or black, odd or even, 1-18 or 19-36 etc.  This output is then captured into a list which is referenced as metadata of the spun number.  The list is then compared against the type of bet and matched, if matched, then there is a win and payout is made.

Each win payout has the same check to make sure that the user is betting up to the amount in the balance and not over (you will get an error message if you try to bet $25 when all you have is $20 to bet).  This section of the code could be extracted into it's own function to simplify the code, which again, could be seen as an opportunity to refactor the code.

To play they game you will have to enter the value you want to bet exactly as stated (example odd or even  not Odd or Even).  Still lots of room for improvement but at this point, i'll leave it here for others to fork and try to enhance.  One good example, the actual one I'll be pursuing, is to replace the options "odd" or "even" with "1. Odd" or "2. Even" and as the user to enter 1 or 2.    Also, please note that 00 is still not coded for and this would require changes to the input function asking for a number as 00 would need to be accepted as a string and right now that code is immediately converting every number from str to int().

Best of luck. 
