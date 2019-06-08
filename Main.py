class Hero :

	def __init__(self,name,health):
		self.name = name
		self.health= health

	@property
	def info(self):
		pass

	@info.getter
	def info(self):
		print("{} punya health {}".format(self.name,self.health))

class Hero_intelligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)


class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name,200)

sniper = Hero("sniper",100)
#axe	= Hero_strength('axe')
lina	=Hero_intelligent('lina')


#print(sniper.info())
#print(axe.__dict__)

lina.info

