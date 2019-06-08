class Hero :

	def __init__(self,name,health):
		self.name = name
		self.healthBase = health

class Hero_intelligent(Hero):
	pass

class Hero_strength(Hero):
	pass

sniper = Hero("sniper",100)
axe	= Hero_strength('axe',200)

lina	=Hero_intelligent('lina',90)

print(sniper.name)
print(lina.__dict__)

print(axe.name)
