class Hero :

    count = 0
    __privateCount=0

    def __init__(self,name,health) :
        self.name   =   name
        self.health =   health

        # variable instance private
        self.__private = "private"

        # variable instance protected
        self._protected = "protected"

lina    =   Hero("lina",100)

print(lina.__dict__)
# lina.private = "tes saja"