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

    # method tanpa return 
    def siapa(self) :
        print("nama ku adalah " + self.name)
    
    # method dengan argument tanpa reaturn
    def healthUp(self,up):
        self.health += up

    # method dengan return 
    def getHealth(self) :
        return self.health

sniper  = Hero('sniper',100,10,5)
cai     = Hero('cai',90,5,10)

sniper.siapa()
sniper.healthUp(10)
print("health ", sniper.getHealth())
