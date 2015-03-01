class mapSelect():
	def __init__(self,cityName,buttonX,buttonY):
		self.cityName = pygame.image.load("ASSETS\ ",cityName,".png")
		self.cityName = pygame.transform.scale(self.cityName,(130,100))
		self.display.blit(self.cityName,(buttonX,buttonY))

		def cityText(self,textFont,textSize,textLocationX,textLocationY,textStatment,textColour):
			self.font = pygame.self.font.Font(textFont, textSize)
			self.text = self.font.render(textStatment,1,textColour)
			self.display.blit(self.text,(textLocationX,textLocationY))