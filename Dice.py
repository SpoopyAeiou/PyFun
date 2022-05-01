from random import randint

def roll_die(die):
    n,d = die.split('d')
    dice = randint(int(n),int(d) * int(n))
    return(dice)