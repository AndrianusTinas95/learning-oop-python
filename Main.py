class Hero :

	__expBase=100

	def __init__(self,name):
		self.__health_pool= [0,100,200,300,400]
		self.__attPower_pool =[0,20,50,80,100]
		self.__armor_pool =[0,2,4,6,8]

		self.__name=name
		self.__exp =0
		self.__level=0

	@property
	def info(self):
		pass

	@info.getter
	def info(self):
		print("{} punya health {}".format(self.__name,self.__health))

	@property
	def health_pool(self):
		pass

	@health_pool.setter
	def health_pool(self,input):
		 self.__health_pool=input

	@property
	def attPower_pool(self):
		pass

	@attPower_pool.setter
	def attPower_pool(self,input):
		self.__attPower_pool= input

	@property
	def armor_pool(self):
		pass

	@armor_pool.setter
	def armor_pool(self,input):
		self.__armor_pool=input

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self,input):
		self.__exp=input
		if self.__exp >= __expBase :
			self.levelUp =  self.__exp // __expBase
			self.__exp %=__expBase

	@property
	def levelUp(self):
		pass

	@levelUp.setter
	def levelUp(self,input):
		self.__level=input
		self.__health =self.__health_pool[self.__level]
		self.__attPower=self.__attPower_poll[self.__level]
		self.__armor=self.__armor_pool[self.__level]

class Hero_intelligent(Hero):
	def __init__(self,name):
		super().__init__(name)

	#override
	@property
	def info(self):
		pass

	@info.getter
	def info(self):
		print('{} tipe {} punya health {}'.format(
			self.name,'intelligent',self.health
			)
		)

class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name)
		self.health_pool=[0,200,400,600,800]
		self.attPower_pool=[0,10,20,30,40]
		self.armor_pool =[0,0.5,1,1.5,2]
		self.levelUp=1

axe	= Hero_strength('axe')
lina	=Hero_intelligent('lina')



#lina.info
axe.info

