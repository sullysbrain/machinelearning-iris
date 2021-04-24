"""Rock, Paper, Scissors Game

This script allows the user to play a game of Rock, Paper, Scissors against the computer.
The user selects one of three options and the computer then plays.
The game repeats if the player ties or loses and continues until the player wins."""


import random

def returnPlayString(value: int) -> str:
    """A function to take a numerical value inputed from the user and returns a string of what the user played"""
    if 0 < value & value < 4:
        if value == 1:
            return "Rock"
        elif value == 2:
            return "Paper"
        else:
            return "Scissors"
    else:
        return ""

def getValidSelections():
    """Validates that a user typed a selection within the bounds. Repeats until input is valid."""
    playerSelectionNotValid = True
    while playerSelectionNotValid:
        playerSelection = input("Select: 1) Rock 2) Paper 3) Scissors: ")
        if ((int(playerSelection) > 0) & (int(playerSelection) < 4)):
            playerSelectionNotValid = False
        else:
            print("Please make a valid selection.\n")
    return int(playerSelection)



def main():
    playerWon = False;
    while not playerWon:
        playerInt = getValidSelections()
        computerInt = random.randint(1, 3)
        print("You chose: " + returnPlayString(playerInt) + ". Computer chose " + returnPlayString(computerInt) + ". ")
        if playerInt == computerInt:
            print("Tie. You both played " + returnPlayString(playerInt) + "\n")
        elif ((playerInt == 1) & (computerInt == 3)) | ((playerInt == 2) & (computerInt == 1)) | ((playerInt == 3) & (computerInt == 2)):
            print(returnPlayString(playerInt) + " beats " + returnPlayString(computerInt) + ". You won!\n")
            playerWon = True
        else:
            print(returnPlayString(computerInt) + " beats " + returnPlayString(playerInt) + ". You lose.\n")


if __name__ == "__main__":
    main()
