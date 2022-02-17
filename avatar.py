import random
class avatar:
    def __init__(self,name,life,strength,protection):
        self.name = name
        self.life = life
        self.strength = strength
        self.protection = protection
        
        
    def attack(self)->int:
        return self.strength     
    def defend(self)->int:
        return self.protection

class warrior(avatar):
    def __init__(self,name,life,strength,protection,shield,fury):
        self.shield = shield
        self.fury = fury
        super().__init__(name,life, strength,protection)
    def attack(self)->int:
        return self.strength + random.randint(0, self.fury)
    
    def defend(self)->int:
        return self.shield + self.protection
 
class mage(avatar):
    def __init__(self,name,life,strength,protection,mana):
        self.mana = mana
        
        super().__init__(name,life, strength,protection)
        
    def attack(self)->int:
        self.mana += random.randrange(0,3,2)
        if self.mana > 1:
            self.mana -= 1
            return self.strength
        elif self.mana >0:
            self.mana -=1
        else:  
            return 1
    
    def defend(self)->int:
        return self.protection
    
class priest(avatar):
    def __init__(self,name,life,strength,protection,mana):
        self.mana = mana
        super().__init__(name,life, strength,protection)
        
    def attack(self)->int:
        self.mana += random.randrange(0,3,2)
        if self.mana > 1:
            self.mana -= 1
            return self.strength
        if self.mana >0:
            self.mana -=1  
            return 1   
    def defend(self)->int:
        return self.protection

    def heal(self)->int:
        self.mana += random.randrange(0,3,2)
        if self.mana > 2:
            self.mana -= 2
            return self.strength//2

        if self.mana >1:
            self.mana -= 2
        return 0
   
    
class chaman(avatar):
    def __init__(self,name,life,strength,protection,mana):
        self.mana = mana
        super().__init__(name,life, strength,protection)
        
    def attack(self)->int:
        return self.strength   
    def defend(self)->int:
        return self.shield + self.protection

    def heal(self)->int:
        self.mana += random.randrange(0,3,2)
        if self.mana > 2:
            self.mana -= 2
            return self.strength//3

        if self.mana >1:
            self.mana -= 2
        return 0
    
player1 = warrior('warrior1',120,80,20,23,4)
player2 = mage('mage1',120,80,20,0)
player3 = priest('priest1',120,80,20,1)
player4 = chaman('priest1',120,80,20,1)

print(player1.attack())
print(player2.attack())
print(player3.heal())
print(player4.heal())


        
        
        