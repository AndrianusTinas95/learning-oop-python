class Hero:
	def __init__(self,name,health):
		self.name =name
		self.health=health

	def showInfo(self):
		print("{} health : {}".format(self.name,self.health))

class Hero_Intelligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)

	def showInfo(self):
		print("{} \n\tTipe : Intelligent , \n\thealth : {}".
			format(self.name,self.health)
		)

class Hero_Strength(Hero):
	def __init__(self,name):
		super().__init__(name,200)


lina = Hero_Intelligent('lina')
axe = Hero_Strength('axe')


lina.showInfo()
axe.showInfo()
