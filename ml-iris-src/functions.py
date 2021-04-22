
import random

def playGame():
    r1 = random.randint(0, 2)
    if r1 == 0:
        return "rock"
    elif r1 == 1:
        return "paper"
    else: 
        return "scissors"


# lost = False;

for x in range(10):
    print("Game " + str(x) + ": " + playGame())





