class Hero :

	def __init__(self,name,health):
		self.name = name
		self.health= health

class Hero_intelligent(Hero):
	def __init__(self,name):
#		Hero.__init__(self,name)
 		super().__init__(name,100)

class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name,200)

sniper = Hero("sniper",100)
axe	= Hero_strength('axe')
lina	=Hero_intelligent('lina')

#print(sniper.name)
print(lina.__dict__)

print(axe.__dict__)
