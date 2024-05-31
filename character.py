class Character():
    maxHp = 0
    hp = 0
    tempHp = 0
    armor = 0
    name = "superduperduperdupersuperlong"
    hasInspiration = False
    def __init__(self):
        pass

    def incHp(self):
        if(self.hp < self.maxHp):
            self.hp += 1

    def decHp(self):
        self.hp -= 1

    def changeHp(self,number):
        self.hp += number

    def setName(self,new):
        self.name = new
        print(self.name)