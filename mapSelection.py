import pygame
import Image
import sys
class mapSelect():
	def mapPanel(self):
		pygame.init()

		#create display
		self.size = width, height = 600, 600
		self.display = pygame.display.set_mode(self.size)
		#pygame.display.set_catption("Map Selection")

		#load in button images
		self.London = pygame.image.load("London.png")
		self.Paris = pygame.image.load("Paris.png")
		self.NewYork = pygame.image.load("New York.png")
		self.Tokyo = pygame.image.load("Tokyo 2.png")
		self.Johnasabergg = pygame.image.load("Johnasabergg.png")
		self.Berlin = pygame.image.load("Berlin.png")

		#make all the images the same size
		self.London = pygame.transform.scale(self.London,(100,100))
		self.Paris = pygame.transform.scale(self.Paris,(100,100))
		self.NewYork = pygame.transform.scale(self.NewYork,(100,100))
		self.Tokyo = pygame.transform.scale(self.Tokyo,(100,100))
		self.Johnasabergg = pygame.transform.scale(self.Johnasabergg,(100,100))
		self.Berlin = pygame.transform.scale(self.Berlin,(100,100))

		self.display.blit(self.London,(100,100))
		self.display.blit(self.Paris,(250,100))
		self.display.blit(self.NewYork,(400,100))
		self.display.blit(self.Tokyo, (100,300))
		self.display.blit(self.Johnasabergg, (250,300))
		self.display.blit(self.Berlin, (400,300))

		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:sys.exit()

map1 = mapSelect()
map1.mapPanel()


