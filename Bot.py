import Dice

def selector():
    x = input("What dice would you like to roll?")
    if x == "d20":
        print(Dice.d20())
    else:
        print("Not a dice!")
selector()