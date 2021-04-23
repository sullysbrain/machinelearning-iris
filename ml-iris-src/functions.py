import random

playerWon = False;

def returnPlayString(value):
    if 0 < value & value < 4:
        if value == 1:
            return "Rock"
        elif value == 2:
            return "Paper"
        else:
            return "Scissors"
    else:
        return ""


while not playerWon:
    player = input("Select: 1) Rock 2) Paper 3) Scissors: ")
    playerInt = int(player)
    computerInt = random.randint(1, 3)
    print("You chose: " + returnPlayString(playerInt) + ". Computer chose " + returnPlayString(computerInt) + ". ")
    if playerInt == computerInt:
        print("Tie. You both played " + returnPlayString(playerInt) + "\n")
    elif ((playerInt == 1) & (computerInt == 3)) | ((playerInt == 2) & (computerInt == 1)) | ((playerInt == 3) & (computerInt == 2)):
        print(returnPlayString(playerInt) + " beats " + returnPlayString(computerInt) + ". You won!\n")
        playerWon = True
    else:
        print(returnPlayString(computerInt) + " beats " + returnPlayString(playerInt) + ". You lose.\n")
