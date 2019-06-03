class Hero:
    
    count = 0    
    def __init__(self,name,health,power,armor):
        self.name   = name
        self.health = health
        self.power  = power
        self.armor  = armor
        Hero.count  +=1

    def attack(self, lawan) :
        print(self.name + " menyerang " + lawan.name)
        lawan.attacked(self)

    def attacked(self, lawan) :
        print(self.name + " diserang " + lawan.name)

        attack_received = lawan.power / self.armor
        print("serangan sebesar " + str(attack_received))

        self.health -= attack_received
        print("darah " + self.name + " sekarang tersisa " , str(self.health))

sniper      = Hero('sniper', 100 ,20, 5)
rikimaru    = Hero('rikimaru',200,10,10)

sniper.attack(rikimaru)
print("\n")
rikimaru.attack(sniper)
rikimaru.attack(sniper)
rikimaru.attack(sniper)
rikimaru.attack(sniper)
