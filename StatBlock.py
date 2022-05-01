import Dice
class statblock():

    statblocks = {}

    def __init__(self,name,stre,dex,con,ddie,hdie):
        statblock.statblocks[name] = self
        self.name = name
        self.str = stre
        self.dex = dex
        self.con = con
        hdie = hdie.split('d')
        self.health = int(int(hdie[0]) * ((int(hdie[1]) / 2)) + ((con - 10) // 2) * int(hdie[0]))
        self.ac = 10 + (dex - 10) // 2
        self.ddie = ddie
    def attack(self, ac):
        tohit = Dice.roll_die('1d20') + (self.str - 10) // 2
        if tohit >= ac:
            dmg = Dice.roll_die(self.ddie) + (self.str - 10) // 2
        else:
            dmg = 0
        return dmg
    def __str__(self):
        block = 'Name - ' + self.name + '\nStr - ' + str(self.str) + '\nDex - ' + str(self.dex) + '\nCon - ' + str(self.con) + '\nHealth - ' + str(self.health) + '\nAC - ' + str(self.ac) + '\nDamage Die - ' + self.ddie + '\n'
        return block
Goblin = statblock('Goblin',12,14,10,'1d6','1d8')