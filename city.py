from gen_arena import arena

class city():

	def __init__(self, cityName, treasuresList):
		
		self.__name = cityName 
		self.arena = arena(self.__name, treasuresList)   #Create a new instance of an arena in the city class.
		self.__image = self.arena.ret_image() 
                print "City setup finished"

		
