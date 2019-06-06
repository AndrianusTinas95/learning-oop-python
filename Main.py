class Hero :

	__count = 0
	__expBase = 5

	def __init__(self,name,health,attPower,armor) :
		self.__name = name
		self.__healthBase = health
		self.__attPowerBase = attPower
		self.__armorBase = armor

		self.__exp = 0
		self.__level = 1
		self.__setInfo()

	def __setInfo(self):
		self.__healthMax = self.__healthBase * self.__level
		self.__attPower = self.__attPowerBase * self.__level
		self.__armor	= self.__armorBase * self.__level
		self.__health	= self.__healthMax

		Hero.__count	+=1

	@property
	def info(self) :
		return "{} => \n\tlevel : {} \n\thealth :{}/{} \n\tpower : {}\n\tarmor : {} ".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self,expUp):
		self.__exp += expUp
		if(self.__exp >= self.__expBase):
			print(self.__name, ' level up ' )
			self.__level +=1
			self.__exp -=self.__expBase

			self.__setInfo()

	def attack(self,enemy) :
		attacked = self.__attPower / enemy.__armor

		self.gainExp = attacked
		enemy.__health -=attacked

		if(enemy.__health <= 0) :
			print('======================')
			print(enemy.__name,' is death')
			print('======================')





sniper = Hero("sniper",10,10,5)
axe	= Hero("axe",15,5,10)
cai	= Hero("cai",5,25,25)

print(sniper.info)
for x in range(11):
	print('sniper attack axe')
	sniper.attack(axe)

print(cai.info)
for x in range(8):
	print('cai attack sniper')
	cai.attack(sniper)

print('°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('end game info')
print('__________________________')
print(cai.info)
print(sniper.info)
print(axe.info)



