class Hero :

    # __count = 0

    def __init__(self,name,health,armor) :
        self.name = name
        self.__health = health
        self.__armor = armor
        # Hero.__count += 1
        # self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def info(self) :
        return  "name {} : \n\thealth: {}".format(self.name,self.__health)
   
    @property
    def armor(self) :
        pass
    
    @armor.getter
    def armor(self) :
        return self.__armor
   
    @armor.setter
    def armor(self, input) :
        self.__armor = input
    
    @armor.deleter
    def armor(self) :
        print("armor di delete")
        self.__armor = None
   

sniper = Hero("sniper",100,10)
print(sniper.info)
sniper.name ="cai"
print(sniper.info)

print("\nget and set __armor")
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 20
print(sniper.armor)
print(sniper.__dict__)

print("delet armor")

del sniper.armor
print(sniper.__dict__)
