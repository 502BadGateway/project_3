class mapSelect():
	def __init__(self):
		self.cityName = pygame.image.load("ASSETS",cityName,".png")
		self.cityName = pygame.transform.scale(self.cityName,(130,100))
		self.display.blit(self.cityName,(buttonX,ButtonY))

		def cityText(self):
			self.font = pygame.self.font.Font(None, 20)
			self.text = self.font.render("Please select you desired location",1,(10,10,10))
			self.display.blit(self.text,(28,12))