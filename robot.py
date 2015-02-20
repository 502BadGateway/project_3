class Robot:

	def __init__(self): #Constructor
		pygame.sprite.Sprite.__init__(self)
		if Robot.image is none:             #What is this meant to be doing?
			Robot.image = pygame.image.load("robot.png")

		self.image = Robot.image
		self.name = ""
		self.points = ""
		self.rect = Robot.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0


    def moveUp(self):   #move robot functions
		
    def moveDown(self):  #move robot functions  

    def moveLeft(self):  #move robot functions 

    def moveRight(self):  #move robot functions

    def returnLocationX():  #Return the X location of the bot
        return self.rect.x

    def returnRectY(self):  #Return the Y location of the bot
        return self.rect.y

    def returnPoints(self):
        return self.points



