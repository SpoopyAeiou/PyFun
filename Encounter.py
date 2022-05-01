import Dice
import StatBlock

class alive():


    def __init__(self,name,block):
        self.name = name
        self.block = StatBlock.statblock.statblocks[block]
        self.health = self.block.health
    def take_dmg(self,dmg):
        self.health -= dmg
        if self.health <= 0:
            del(self)
def goblinattack():
    print(StatBlock.Goblin.attack(10))
print(StatBlock.Goblin)

G1 = alive('G1', 'Goblin')
G2 = alive('G2', 'Goblin')
while G1 and G2:
    G2.take_dmg(G1.block.attack(G2.block.ac))
    G1.take_dmg(G2.block.attack(G1.block.ac))
print('Done')