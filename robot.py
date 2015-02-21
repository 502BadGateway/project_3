class Robot:

	def __init__(self): #Constructor
		pygame.sprite.Sprite.__init__(self)
		if Robot.__image is none:             #What is this meant to be doing?
			Robot.__image = pygame.image.load("robot.png")

		self.__image = Robot.image
		self.__name = ""
		self.__points = ""
		self.__rect = Robot.__image.get_rect()
		self.__rect.x = 0
		self.__rect.y = 0


    def moveUp(self):   #move robot functions
		
    def moveDown(self):  #move robot functions  

    def moveLeft(self):  #move robot functions 

    def moveRight(self):  #move robot functions

    def returnLocationX():  #Return the X location of the bot
        return self.__rect.x

    def returnRectY(self):  #Return the Y location of the bot
        return self.__rect.y

    def returnPoints(self):
        return self.__points



