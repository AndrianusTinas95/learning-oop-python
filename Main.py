class Hero :

    __count = 0

    def __init__(self,name) :
        self.__name = name
        # self.__health = health
        # self.__power = power
        Hero.__count += 1

    # berlaku untuk object
    def getCount(self) :
        return Hero.__count

    #berlaku untuk class
    def getCountA() :
        return Hero.__count
    
    # method static (decorator)
    @staticmethod
    def getCountB() :
        return Hero.__count
    
    @classmethod
    def getCountC(cls) :
        return cls.__count

sniper    = Hero("sniper")
print(Hero.getCountB())
rikimaru  = Hero("rikimaru")
print(sniper.getCountC())
drowranger= Hero("drowranger")
print(Hero.getCountC())
