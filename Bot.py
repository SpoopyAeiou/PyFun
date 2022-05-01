import Dice
from random import randint
def selector():
    x = input("What dice would you like to roll? ")
    if x == "d20" or x == "D20":
        print(Dice.d20())
    elif x == "d12" or x == "D12":
        print(Dice.d12())
    elif x == "d10" or x == "D10":
        print(Dice.d10())
    elif x == "d8" or x == "D8":
        print(Dice.d8())
    elif x == "d6" or x == "D6":
        print(Dice.d6())  
    elif x == "d4" or x == "D4":
        print(Dice.d4())
    elif x == "custom" or x == "Custom":
        c = int(input("Oh? How many sides? "))
        print(Dice.custom(c))  
    else:
        print("Not a dice!")   

def roll_die(die):
    n,d = die.split('d')
    dice = randint(int(n),int(d) * int(n))
    return(dice)
print(roll_die(input("Input your dice : ")))