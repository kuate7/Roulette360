# Roulette 360 App

## Overview
The purpose of this repo is to enable best practice code collaboration for the gptx360devteam.

The code itself will mirror the casino game Roulette.

`roulette.py` is the main logic of the project. Here the code is broken down into smaller functions that serve a purpose.  To start out, the roulettespin() function gets us a simulated random spin which is then passed to the secondary functions to read what that number translates to i.e. Red or black, odd or even, 1-18 or 19-36 etc.  This output is then captured into a list which is referenced as metadata of the spun number.  The list is then compared against the type of bet and matched, if matched, then there is a win and payout is made.

Each win payout has the same check to make sure that the user is betting up to the amount in the balance and not over (you will get an error message if you try to bet $25 when all you have is $20 to bet).  This section of the code could be extracted into it's own function to simplify the code, which again, could be seen as an opportunity to refactor the code.

To play they game you will have to enter the value you want to bet exactly as stated (example odd or even  not Odd or Even).  Still lots of room for improvement but at this point, i'll leave it here for others to fork and try to enhance.  One good example, the actual one I'll be pursuing, is to replace the options "odd" or "even" with "1. Odd" or "2. Even" and as the user to enter 1 or 2.    Also, please note that 00 is still not coded for and this would require changes to the input function asking for a number as 00 would need to be accepted as a string and right now that code is immediately converting every number from str to int().

Best of luck.

## Getting Started
Ensure the following technologies are installed and configured:
- git
- python
- pip
- make
- An IDE, such as Visual Studio Code or Atom

### Clone the Repo
`git clone https://github.com/kuate7/Roulette360.git`

This will create a local copy of the repo in a directory called `Roulette360`
wherever you executed this command.

### Making Changes
- Ensure you have the latest code changes present in your local repo: `git pull`
- First, create your own branch based off of `master`: `git checkout -b myNewBranchName`
- Make your changes, and then verify your changes with `git status`
- Add your changes: `git add .` (adds all changed files) OR `git add someSpecificFile.py`
- Commit your changes: `git commit -m "Did thing to stuff"`
- Push your changes: `git push origin`
- Make a Pull Request to the `master` branch from your `myNewBranchName` branch using GitHub.com

### Using the Makefile

#### Install all dependencies of the project
`make init`

#### Run all automated tests for project
`make test`
