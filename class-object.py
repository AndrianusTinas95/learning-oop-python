class Hero:
    # class variable
    count = 0    
    def __init__(self,name,health,power,armor):
        # is instance variablr
        self.name   = name
        self.health = health
        self.power  = power
        self.armor  = armor
        Hero.count  +=1

        print("Membuat hero dengan nama " + name)

hero1   = Hero("sniper",100,10,4)
print(Hero.count)
hero2   = Hero("sniper",100,15,1)
print(Hero.count)
hero3   = Hero("sniper",1000,100,0)
print(Hero.count)
