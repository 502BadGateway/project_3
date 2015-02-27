import gen_arena

class city():

	def __init__(self, cityName):
		
		self.name = ""
		self.arena = arena(cityname)   #Create a new instance of an arena in the city class.
		self.image = self.arena.ret_image() 
		
