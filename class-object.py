class Hero:
    name = "cai"    
    def __init__(self,name,health,power,armor):
        self.name   = name
        self.health = health
        self.power  = power
        self.armor  = armor

hero1   = Hero("sniper",100,10,4)
hero2   = Hero("sniper",100,15,1)
hero3   = Hero("sniper",1000,100,0)

print(hero1.name)
print(hero2.health)
print(hero3.__dict__)