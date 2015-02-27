#Entity class. Should be VERY similar to landmarks class from last project

class entity:
	def __init__(self, name, val):
		self.__name = ""
        self.__arenaValue = val #Value representing this object in the arena


    def getName(self):
        return self.__name

    def getArenaValue(self):
        return self.__arenaValue
		
