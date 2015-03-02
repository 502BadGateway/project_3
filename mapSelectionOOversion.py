class mapSelect():
	def __init__(self,cityName,buttonX,buttonY,imageLocation,buttonHeight,buttonWidth):
		self.cityName = pygame.image.load(self.imageLocation)
		self.cityName = pygame.transform.scale(self.cityName,(buttonHeight,buttonWidth))
		self.display.blit(self.cityName,(buttonX,buttonY))

		def cityText(self,textFont,textSize,textLocationX,textLocationY,textStatment,textColour):
			self.font = pygame.self.font.Font(textFont, textSize)
			self.text = self.font.render(textStatment,1,textColour)
			self.display.blit(self.text,(textLocationX,textLocationY))