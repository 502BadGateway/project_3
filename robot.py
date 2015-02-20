class Robot:

	def __init__(self): #Constructor
		pygame.sprite.Sprite.__init__(self)
		if Robot.image is none:
			Robot.image = pygame.image.load("robot.png")
		self.image = Robot.image
		self.name = ""
		self.points = ""
		self.rect = Robot.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0


    def moveUp(self):
		
    def moveDown(self):

    def moveLeft(self):

    def moveRight(self):

    def returnLocationX():
        return self.rect.x

    def returnRectY(self):
        return self.rect.y


