import gen_arena

class city():

	def __init__(self, cityName):
		
		self.__name = cityName 
		self.__arena = arena(cityname)   #Create a new instance of an arena in the city class.
		self.__image = self.arena.ret_image() 
		
