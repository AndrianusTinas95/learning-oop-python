class Hero :

    count = 0

    def __init__(self,name,health,power) :
        self.__name = name
        self.__health = health
        self.__power = power
    
    # getter
    def getName(self) :
        return self.__name
    
    def getHealth(self) :
        return self.__health
    
    #setter
    def attacked(self,attackPower) :
        self.__health -= attackPower
    
    def setPower(self,power) :
        self.__power = power


#awal game
earthshaker = Hero("earthshaker",50,5)

#game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.attacked(5)

print(earthshaker.getHealth())
